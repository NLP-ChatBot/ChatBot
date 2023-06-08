# imports
import torch.nn as nn
import torch



class ChatBot(nn.Module):

    def __init__(self, in_f: int, out_shape: tuple, word_dict: dict, device: str) -> None:
        super(ChatBot, self).__init__()
        
        self.w, self.len = out_shape
        self.len -= 1
        self.wd = word_dict
        self.dv = device
        
        self.l_h = nn.Linear(in_features=in_f, out_features=1024)
        self.l_c = nn.Linear(in_features=in_f, out_features=1024)
        
        self.emb = nn.Embedding(num_embeddings=self.w, embedding_dim=self.len)
        self.lstm = nn.LSTM(input_size=in_f + self.len, hidden_size=1024, bias=True, batch_first=True)
        self.lin = nn.Linear(in_features=1024, out_features=self.w)
        self.drop = nn.Dropout(p=0.3)
        
        self.to(device=device)
    
    def forward(self, question, answer) -> torch.Tensor:
        
        pred = torch.zeros(size=[question.size(0), self.w, self.len]).to(device=self.dv)

        h, c = self.init_memory(x=question.float())
        
        answer = self.emb(answer.long())

        for idx in range(self.len):
            
            out, (h, c) = self.lstm(torch.cat(tensors=(question, answer[:,0]), dim=1), (h, c))
            out_lin = self.lin(self.drop(out))
            
            pred[:,:,idx] = out_lin
        
        return pred
    
    def gen_text(self, question) -> torch.Tensor:
        
        pred = torch.zeros(size=(question.size(0), self.w, self.len)).to(device=self.dv)
        init_word = torch.tensor(data=[self.wd['<start>']]).to(device=self.dv)
        
        h, c = self.init_memory(x=question.float())
        words = self.emb(init_word.long())
        
        for word_idx in range(self.len):
            
            out, (h,c) = self.lstm(torch.cat(tensors=(question, words[:,0]), dim=1), (h,c))
            out_lin = self.lin(self.drop(out))
            
            pred[:,:,word_idx] = out_lin
            
            words = self.emb(out_lin)

            if out_lin.argmax() == self.wd['<stop>']:
                break

        return pred
    
    def init_memory(self, x) -> torch.Tensor:

        h = self.l_h(x)
        c = self.l_c(x)

        return h, c
