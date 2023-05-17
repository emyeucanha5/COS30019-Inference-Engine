from Algorithm import Algorithm
from BackwardChaining import BackwardChaining
from KnowledgeBase import KnowledgeBase
from TruthTable import TruthTable
from ForwardChaining import ForwardChaining
from DPLL import DPLL
class Engine:
    def __init__(self) -> None:
        self.method = "tt"
        self.knowledge_base = KnowledgeBase()
        self.algorithm: Algorithm = None
        
    def do_algorithm(self) -> bool:
        ans = None
        self.method = self.method.lower()
        if(self.method == "tt"):
            self.algorithm = TruthTable(self.knowledge_base)
            ans = self.algorithm.entails()
        if(self.method == "fc"):
            self.algorithm = ForwardChaining(self.knowledge_base)
            ans = self.algorithm.entails()
        if(self.method == "bc"):
            self.algorithm = BackwardChaining(self.knowledge_base)
            ans = self.algorithm.entails()
        if(self.method == "dpll"):
            self.algorithm = DPLL(self.knowledge_base)
            ans = self.algorithm.entails()
        if(ans[0] == True):
            
            print("YES: ", end="")
            if(self.method == "bc" or self.method == "fc"):
                for i, val in enumerate(ans[1]):
                    print(val, end="")
                    if(i < ans[1].__len__() - 1):
                        print(", ", end="")
                    else:
                        print()
            elif(self.method == "tt"):
                print(ans[1])
            elif(self.method == "dpll"):
                return
        else:
            print("NO")
        return True
    
    def set_method(self, method: str) -> None:
        self.knowledge_base.method = method
        self.method = method