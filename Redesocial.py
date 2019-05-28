import string
# Contentor para guardar um item numa lista bidireccional
class Contentor2:

    def __init__(self,item,seguinte,anterior):
        self.item=item
        self.seguinte=seguinte
        self.anterior=anterior

    def __str__(self):
        return str(self.item)

# ---------------------------------------

# Lista bidireccional com topo e fim
class Lista3:

    def __init__(self):
        self.topo=None
        self.fim=None

    def __str__(self):
        s= "["
        actual = self.topo
        while actual!=None:
            s+= str(actual)
            if actual.seguinte != None:
                s+=","
                actual =actual.seguinte
        s += "]"
        return s
        



    # Junta um elemento ao inicio da lista
    def juntaInicio(self,item):
        elem=Contentor2(item,None,None)
        if self.topo==None:
            self.topo=elem
            self.fim=elem
        else:
            elem.seguinte=self.topo
            self.topo.anterior=elem
            self.topo=elem

    # Junta um elemento ao final da lista
    def juntaFim(self,item):
        if self.topo==None:
            self.juntaInicio(item)
        else:
            elem=Contentor2(item,None,self.fim)
            self.fim.seguinte=elem
            self.fim=elem

    # Apaga um elemento do inicio da lista e devolve esse elemento
    def apagaInicio(self):
        if self.topo==None:
            return None
        elif self.topo==self.fim:
            item=self.topo.item
            self.topo=None
            self.fim==None
        else:
            item=self.topo.item
            self.topo=self.topo.seguinte
            self.topo.anterior=None


    # Apaga um elemento do fim da lista e devolve esse elemento
    def apagaFim(self):
        if self.topo==None:
            return None
        elif self.topo==self.fim:
            item=self.topo.item
            self.topo=None
            self.fim==None
        else:
            item=self.fim.item
            self.fim=self.fim.anterior
            self.fim.seguinte=None

    # Elimina um elemento da lista bidireccional NOVO UPDATE
    def eliminaelemento(self,item):
        actual = self.topo
        while actual != None:
            if (item == actual.item) and (actual.seguinte ==None):
                self.apagaFim()
            elif (item==actual.item) and (actual.anterior ==None):
                self.apagaInicio()
            elif item == actual.item:
                actual.anterior.seguinte = actual.seguinte
                actual.seguinte.anterior=actual.anterior
            actual=actual.seguinte
    def contagem(self):
        if self.topo== None:
            return 0
        else:
            s=0
            actual = self.topo
            while actual != None:
                s+=1
                actual = actual.seguinte
            return s
                
                
########################################################################            
            
            
class User:
    def __init__(self,email,passwd):
        self.e=email
        self.false = passwd
        self.password = passwd
        self.estado= 'ativa'
        self.name = None
        self.data = None
        self.setPassword(self.password)
        self.listaamigos = Lista3()
        self.listapedidos= Lista3()

    def __str__(self):
        if self.name == None:
            return str(self.e)+":"+self.estado
        return str(self.name) + ':' + str(self.e) + ':' + self.estado

    def getEmail(self):
        return str(self.e)

    def setPassword(self,passwd):
        string.lower(passwd)==passwd
        password=''
        for i in passwd:
            if ord(i)>=120:
                password += chr(ord(i)-23)
            else:
                password += chr(ord(i)+3)
        self.password = password

    def getPassword(self):
        return str(self.password)

    def setName(self,name):
        self.name= name

    def getName(self):
        return str(self.name)

    def setBirth(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

    def getBirth(self):
        return "("+str(self.year)+', '+str(self.month)+', '+str(self.day)+')'

    def isActive(self):
        if self.estado=='ativa':
            return True
        else:
            return False

    def setActive(self):
        self.estado= 'ativa'

    def setInactive(self):
        self.estado = 'inativa'

    def setActive(self):
        self.estado= 'ativa'

    def setInactive(self):
        self.estado = 'inativa'

    def askFriend(self,u):
        self.listaamigos.juntaFim(u)

    def recvRequest(self, u):
        self.listapedidos.juntaFim(u)

    def confirmFriend(self, u):
        self.listapedidos.eliminaelemento(u)
        self.askFriend(u)

    def isFriend(self, u):
        if u.e == self.e and u.password == self.password :
            return True
        else:
            return str(u) in str(self.listaamigos)

    def showPending(self):
        actual= self.listapedidos.topo
        if actual==None:
            print ''
        else:
            while actual!=None:
                print actual
                actual= actual.seguinte
    def showFriends(self):
        actual=self.listaamigos.topo
        if actual==None:
            print ''
        else:
            while actual!=None:
                print actual
                actual = actual.seguinte
                

######################################################################

class Post:
    def __init__(self, u, text ="", link=None):
        self.proprio= u
        self.text=text
        self.link=link
        self.likes= Lista3()
        self.dislikes=Lista3()
    def __str__(self):
        if self.text == '' and self.link ==None:
            return '\n' + str(self.likes.contagem())+' Gosto, '+ str(self.dislikes.contagem())+" Nao gosto"
        elif self.text == '' and self.link!= None:
            return str(self.link) + '\n' + str(self.likes.contagem())+' Gosto, '+ str(self.dislikes.contagem())+' Nao gosto'
        elif self.text != '' and self.link== None:
            return str(self.text) + '\n' + str(self.likes.contagem())+' Gosto, '+ str(self.dislikes.contagem())+' Nao gosto'
        else:
            return str(self.text) + '\n' + str(self.link)+ '\n' + str(self.likes.contagem())+' Gosto, '+ str(self.dislikes.contagem())+' Nao gosto'
        
        
            
    def updateText(self,text):
        self.text = str(text)

    def updateLink(self,text):
        self.link = str(text)

    def like(self, u):
        if  self.proprio.isFriend(u) == True:
            self.likes.juntaFim(u)
            self.dislikes.eliminaelemento(u)

    def dislike(self, u):
        if self.proprio.isFriend(u) ==True:
            self.dislikes.juntaFim(u)
            self.likes.eliminaelemento(u)

#############################################################################
class Comments:

    def __init__(self):
        self.comments = Lista3()
        self.comments.topo = None
        

    def __str__(self):
        if self.comments == None:
            print '\n'
        else:
            s=""
            actual=self.comments.topo
            while actual!=None:
                s+=str(actual)
                if actual.seguinte!=None:
                    s+='\n\n'
                actual=actual.seguinte
            return s
            

    def add(self,comment):
        self.comments.juntaInicio(comment)

    def remove(self, comment):
        self.comments.eliminaelemento(comment)

    def countLike(self):
        actual = self.comments.topo
        b = 0
        while actual != None:
            if not '\n0 Gosto' in str(actual):
                b += 1
            actual = actual.seguinte
        return b
        
        
    def showRecentComments(self,n):
        actual = self.comments.topo
        j = 1
        if n == 0:
            print ''
        else:
            while actual != None:
                h=""
                if j <= n:
                    h += str(actual)
                if j < self.comments.contagem() and j<n:
                    h += '\n'
                if j<= n:
                    print h
                j+=1
                actual=actual.seguinte


    def search(self, user = None, likes = None, dislikes = None,text = None):
        commentssearch= []
        Mooshak = Comments()
        actual = self.comments.topo
        while actual !=None:
            commentssearch.append(actual.item)
            actual = actual.seguinte
        print commentssearch
        for i in commentssearch:
            if user != None:
                if not user == i.proprio.e:
                    commentssearch.remove(i)
            if likes != None:
                if likes != i.likes.contagem():
                    commentssearch.remove(i)

            if dislikes != None:
                if dislikes != i.dislikes.contagem():
                    commentssearch.remove(i)
                    
            if text != None:
                if str(text) not in i.text:
                    commentssearch.remove(i)

        for j in commentssearch:
            Mooshak.add(j)

        return Mooshak

u1 = User("luis@gmail.com", "simples")
u2 = User("ana@gmail.com", "complicada")
u2.askFriend(u1)
u1.recvRequest(u2)
u1.confirmFriend(u2)
p1 = Post(u1, "O ultimo post", "http://www.wikipedia.org")
p2 = Post(u2, "A ultima resposta", "http://www.thepiratebay.org")
c = Comments()
c.add(p1)
c.add(p2)




