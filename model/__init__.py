# imports
import torch.nn as nn
import torch



class ChatBot(nn.Module):

    def __init__(self, out_shape: tuple, word_dict: dict, device: str) -> None:
        super(ChatBot, self).__init__()
        
        self.w, self.len = out_shape
        self.len -= 1
        self.wd = word_dict
        self.dv = device
        
        self.q_emb = nn.Embedding(num_embeddings=self.w, embedding_dim=self.len)
        self.q_lstm = nn.LSTM(input_size=self.len, hidden_size=512, bias=True, batch_first=True)
        self.q_lin = nn.Linear(in_features=512, out_features=256)
        
        self.a_emb = nn.Embedding(num_embeddings=self.w, embedding_dim=self.len)
        self.a_lstm = nn.LSTM(input_size=self.len + 256, hidden_size=512, bias=True, batch_first=True)
        
        self.lin = nn.Linear(in_features=512, out_features=self.w)
        self.drop = nn.Dropout(p=0.3)
        
        self.to(device=device)
    
    def forward(self, question, answer) -> torch.Tensor:
        
        pred = torch.zeros(size=[question.size(0), self.w, self.len]).to(device=self.dv)
        
        question = self.q_emb(question.long())
        q_out, (h, c) = self.q_lstm(question)
        q_out = self.q_lin(h)
        
        answer = self.a_emb(answer.long())
        
        for idx in range(self.len):

            input_lstm = torch.cat(tensors=[answer[:,idx].unsqueeze(1), q_out], dim=0)
            out, (h, c) = self.a_lstm(input_lstm, (h, c))
            out_lin = self.lin(self.drop(out.squeeze(1)))
            
            pred[:,:,idx] = out_lin
        
        return pred
    
    def gen_text(self, question) -> torch.Tensor:
        
        pred = torch.zeros(size=(question.size(0), self.w, self.len)).to(device=self.dv)
        init_word = torch.tensor(data=[self.wd['<start>']]).to(device=self.dv)
        
        question = self.q_emb(question.long())
        q_out, (h, c) = self.q_lstm(question)
        q_out = self.q_lin(h)
        
        words = self.a_emb(init_word.long())
        
        for word_idx in range(self.len):

            input_lstm = torch.cat(tensors=[words[:,0].unsqueeze(1), q_out], dim=0)
            out, (h,c) = self.a_lstm(input_lstm, (h,c))
            out_lin = self.lin(self.drop(out.squeeze(1)))
            
            pred[:,:,word_idx] = out_lin
            
            words = self.a_emb(out_lin)

            if out_lin.argmax() == self.wd['<stop>']:
                break

        return pred
