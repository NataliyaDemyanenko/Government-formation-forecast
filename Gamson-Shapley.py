#!/usr/bin/env python3
import tkinter as tk
from tkinter import filedialog
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import pickle
import string
import math
from math import *
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
from itertools import permutations, combinations

def binomial(x, y):
    try:
        binom = math.factorial(x) // math.factorial(y) // math.factorial(x - y)
    except ValueError:
        binom = 0
    return binom

def powerset(s):
    x = len(s)
    masks = [1 << i for i in range(x)]
    for i in range(1 << x):
        yield [ss for mask, ss in zip(masks, s) if i & mask]

class CooperativeGame():
    def __init__(self, characteristic_function):
        if type(characteristic_function) is not dict:
            raise TypeError("characteristic function must be a dictionary")

        temp_ch_f = {}

        for key in characteristic_function:
            if len(str(key)) == 1 and type(key) is not tuple:
                temp_ch_f[(key,)] = characteristic_function[key]
            elif type(key) is not tuple:
                raise TypeError("key must be a tuple")
            else:
                sortedkey = tuple(sorted(list(key)))
                temp_ch_f[sortedkey] = characteristic_function[key]

        self.ch_f = temp_ch_f
        self.player_list = max(characteristic_function.keys(), key=lambda key: len(key))
        self.number_players = len(self.player_list)

    def shapley_value(self):
        payoff_vector = {}
        n = int(len(self.player_list))
        for player in self.player_list:
            weighted_contribution = 0
            for coalition in powerset(self.player_list):
                if coalition:
                    k = int(len(coalition))
                    weight = 1 / (binomial(n, k) * k)
                    t = tuple(p for p in coalition if p != player)
                    weighted_contribution += weight * (self.ch_f[tuple(coalition)] - self.ch_f[t])
            payoff_vector[player] = weighted_contribution

        return payoff_vector

    def is_monotone(self):
        return not any([set(p1) <= set(p2) and self.ch_f[p1] > self.ch_f[p2]
                        for p1, p2 in permutations(self.ch_f.keys(), 2)])

    def is_superadditive(self):
        sets = self.ch_f.keys()
        for p1, p2 in combinations(sets, 2):
            if not (set(p1) & set(p2)):
                union = tuple(sorted(set(p1) | set(p2)))
                if self.ch_f[union] < self.ch_f[p1] + self.ch_f[p2]:
                    return False
        return True

    def __repr__(self):
        return "A {} player co-operative game".format(self.number_players)

    def __latex__(self):
        cf = self.ch_f
        output = "v(c) = \\begin{cases}\n"
        for key in sorted(cf.keys(), key=lambda key: len(key)):
            if not key:
                coalition = "\\emptyset"
            else:
                coalition = "\\{" + ", ".join(str(player) for player in key) + "\\}"
            output += "{}, & \\text{{if }} c = {} \\\\\n".format(cf[key], coalition)
        output += "\\end{cases}"
        return output

    def is_efficient(self, payoff_vector):
        pl = tuple(sorted(list(self.player_list)))
        return sum(payoff_vector.values()) == self.ch_f[pl]

    def nullplayer(self, payoff_vector):
        for player in self.player_list:
            results = []
            for coalit in self.ch_f:
                if player in coalit:
                    t = tuple(sorted(set(coalit) - {player}))
                    results.append(self.ch_f[coalit] == self.ch_f[t])
            if all(results) and payoff_vector[player] != 0:
                return False
        return True

    def is_symmetric(self, payoff_vector):
        sets = self.ch_f.keys()
        element = [i for i in sets if len(i) == 1]
        for c1, c2 in combinations(element, 2):
            results = []
            for m in sets:
                junion = tuple(sorted(set(c1) | set(m)))
                kunion = tuple(sorted(set(c2) | set(m)))
                results.append(self.ch_f[junion] == self.ch_f[kunion])
            if all(results) and payoff_vector[c1[0]] != payoff_vector[c2[0]]:
                return False
        return True

def goldenapp():
    pass
    def powerset(s):
     x = len(s)
     masks = [1 << i for i in range(x)]
     for i in range(1 << x):
         yield [ss for mask, ss in zip(masks, s) if i & mask]


def goldenapp():
     entries={}
     party_names={}
     polls={}

     entries = pickle.load( open( 'save.p', "rb" ) )

     s=0
     party_num=0
     for k in range(0, 15):
         try:
             polls[k]=float(entries[k+1,3])
             s=s+1
         except ValueError:
             party_num=s


     # Initialize parties and coalitions (labelled by letters)

     labels=['']*party_num
     colors=['']*party_num
     partyposition=['']*party_num
     excluded=['']*party_num
   
     parties = list(string.ascii_uppercase)[0:party_num]

     for k in range(0, party_num):
         party_names[k]=str(entries[k+1,0])
         labels[k]=str(entries[k+1,1])
         colors[k]=str(entries[k+1,2])
         excluded[k]=list(str(entries[k+1,4]))


     label = dict(zip(parties,labels))  
     color = dict(zip(parties,colors))
     coalitions = powerset(parties)


     # Introduce campaign commitments

     fr={}
     friends={}
     for k in range(0,party_num):
         fr[k]=list(set(parties) - set(excluded[k]))

     for k in range(0,party_num):
         friends[parties[k]]=fr[k]
         #print(friends[parties[k]])

     # Computing seats, Shapley values and all winning coalitions

     P=0
     for i in range(len(polls)):
         P += polls[i]


     # Initialize proportions of seats (precise and rounded)    

     s ={}
     sround = {}    
     pl = {} 
     i = 0  
     for p in parties:
         pl[p]=polls[i]
         s[p] = polls[i]/P
         sround[p]= round(float(s[p]*100),1)
         i+=1

     worth = {}                                           # Assign worth to coalitions
     mworth = {}
     for i in tuple(coalitions):
         #print(i)
         sumsp=0
         for r in tuple(i):
             j=set(i).intersection(set(friends[r]))
             if j==set(i):
                 sumsp = sumsp +  s[r]
         #print(sumsp)
         worth[tuple(i)]=0
         mworth[tuple(i)]=0
         if (sumsp > 1/2):
             worth[tuple(i)] = 1
             mworth[tuple(i)] =1        
         #worth[tuple(i)] = ( copysign(1,(sumsp - 0.5)) + 1)/2
         #if ( copysign(1,(sumsp - 0.5)) + 1)==1:
             #worth[tuple(i)] = 0
         for j in tuple(powerset(i)):                       # Make game monotonic
             mworth[tuple(i)]=max(mworth[tuple(i)], mworth[tuple(j)])

     #print('Worth', mworth)
     letter_game = CooperativeGame(mworth)
     sh = letter_game.shapley_value()
     #print(sh)
     print( "{:<10} {:<10} {:<10} {:<10} {:<10}".format('Label', 'Party', 'Votes (%)', 'Seats (%)', 'Strength') )
     for k in parties:
         lb = label[k]
         num = sround[k]
         v = sh[k]
         #v = max(sh[k],0)
         print( "{:<10} {:<10} {:<10} {:<10} {:<10}".format(k, lb, round(float(pl[k]),2), num, v) )    

     letter_function = {}
     for k in worth.keys():            # Find all winning coalitions. N: this includes incompatible coalitions also
         if worth[k] != 0:
             letter_function[k]=worth[k]
     #print('Letter function', letter_function)


     # Find all minimal winning coalitions

     non_minimal_winning={}
     for k in letter_function.keys():
         for j in letter_function.keys():
             if (j!= k) and (set(k).intersection(set(j)) == set(k)):             
                 non_minimal_winning[j]=letter_function[j]

     minimal_winning={}
     for k in letter_function.keys():
         if not(k in non_minimal_winning.keys()):
             minimal_winning[k]=letter_function[k] 


     # Find all stable coalitions

     plt.figure(0)                
     chi = {}
     power = {}
     for k in minimal_winning.keys():
         S = 0
         for j in k:
             S += max(sh[j],0)
         chi[k] = minimal_winning[k]/S
         #print(k, chi[k])
         u=''
         b = 0
         for j in k:
             po=''
             pc=''
             power[j] = max(0,sh[j])*chi[k]
             if power[j]==0:
                 po='('
                 pc=')'
             u = u + po + label[j].split('/')[0] + pc + ' '  
         for i in k:
             plt.bar(u, power[i], bottom = b, color = color[i])
             b = b +power[i]
         plt.bar(u, 0.03, bottom=(chi[k]-1)*(0.9), color='white', width=.2) 
     plt.xticks(rotation=-20, fontsize=8, horizontalalignment='left')

        

     #print('Minimal winning coalitions and Power distribution') 
     #print('( Power = Strength x Stability ):')            

     S = 0
     for j in parties:
         S += max(sh[j],0)

     # Calculate stability for all winning coalitions
     chi2 = {}
     for k in letter_function.keys():
         S2 = 0
         for j in k:
             S2 += max(sh[j],0)
         chi2[k] = letter_function[k]/S2
     #print(chi2)


     #Sum of all stability coefficients
     print('Sum of all stability coefficients:')

     SChi2 = sum(chi2.values())
     print(SChi2)

     #Calculate sum of stability (SS) and new stability rank (SR)
     for k in letter_function.keys():
             for j in k:          
                SS = sum(value for key, value in chi2.items() if value >= chi2[k])
                SR = SS / SChi2
             print(k, SS, SR)

     plt.figure(1)                
     for i in parties:
         plt.bar(label[i], s[i], color = color[i], width=0.3, align='center')
         plt.bar(label[i], 0.003, bottom = max(0,sh[i])/S, color = 'red', width=0.6, align='center')         
     plt.xticks(rotation=-20, fontsize=8, horizontalalignment='left')
     
     plt.figure(2)
     G = nx.Graph()
     G.add_nodes_from(parties)
     for i in tuple(parties):
         for j in tuple(parties):
             if set(i).intersection(friends[j])!=set():
                 G.add_edge(i,j)
     pos = nx.spring_layout(G)  # positions for all nodes
     # nodes 
     deg=dict(nx.degree(G))

     nx.draw_networkx_nodes(G, pos, nodelist=parties, node_color=colors, edgecolors='black', alpha=0.5, node_size=[v * 10000 for v in s.values()])
     nx.draw_networkx_nodes(G, pos, nodelist=parties, node_color=colors, edgecolors='red', alpha=0.5, node_size=[v * 10000 for v in sh.values()])

     # edges
     nx.draw_networkx_edges(G, pos, alpha=0.2, width=1.5)
     # labels
     nx.draw_networkx_labels(G, pos, labels=label, font_size=10, font_family='sans-serif')

     plt.axis('off')
     plt.show()
     #print(chi)

# GUI part
entries={}
entry={}
entry_var={}
errmsg = 'Error!'

def load_file():
     FILENAME=askopenfilename()
     try:
        ent = pickle.load( open( FILENAME, "rb" ) )
     except:
        ent={}

     for k in range(0,27):
         for j in range(0,5):
             try:
                 entries[k,j]=ent[k,j]
             except:
                 entries[k,j]=''

def save_file():
     FILENAME = asksaveasfilename()

     for k in range(0,27):
         for j in range(0,5):
             entries[k,j]=entry_var[k,j].get()

     pickle.dump(entries, open(FILENAME, "wb"))

     pickle.dump(entries, open('save.p', "wb"))

def populate():
     load_file()
     for j in range(0,5):
         entry_var[0,j] = tk.StringVar(root, entries[0,j])

     entry[0,0] = tk.Entry(root, width=10, textvariable=entry_var[0,0]).grid(row=0,column=1)
     entry[1,0] = tk.Entry(root, width=10, textvariable=entry_var[0,1]).grid(row=1,column=1)

     for k in range(1,27):
         for j in range(0,5):
             entry_var[k,j] = tk.StringVar(root, entries[k,j])
             entry[k,j] = tk.Entry(root, width=10, textvariable=entry_var[k,j]).grid(row=k+2,column=j+1)



# set the WM_CLASS
root = Tk(className="Goldenapp")
# set the window title
root.wm_title("GoldenApp Political Analytics Tool")


tk.Label(root, text="Country").grid(row=0)
tk.Label(root, text="Poll").grid(row=1)
tk.Label(root, text="Party Name").grid(row=2, column=1)
tk.Label(root, text="Party Label").grid(row=2, column=2)
tk.Label(root, text="Party Color").grid(row=2, column=3)
tk.Label(root, text="Seats Proportion").grid(row=2, column=4)
tk.Label(root, text="Excluded Partners").grid(row=2, column=5)
tk.Label(root, text="A").grid(row=3)
tk.Label(root, text="B").grid(row=4)
tk.Label(root, text="C").grid(row=5)
tk.Label(root, text="D").grid(row=6)
tk.Label(root, text="E").grid(row=7)
tk.Label(root, text="F").grid(row=8)
tk.Label(root, text="G").grid(row=9)
tk.Label(root, text="H").grid(row=10)
tk.Label(root, text="I").grid(row=11)
tk.Label(root, text="J").grid(row=12)
tk.Label(root, text="K").grid(row=13)
tk.Label(root, text="L").grid(row=14)
tk.Label(root, text="M").grid(row=15)
tk.Label(root, text="N").grid(row=16)
tk.Label(root, text="O").grid(row=17)
tk.Label(root, text="P").grid(row=18)
tk.Label(root, text="Q").grid(row=19)
tk.Label(root, text="R").grid(row=20)
tk.Label(root, text="S").grid(row=21)
tk.Label(root, text="T").grid(row=22)
tk.Label(root, text="U").grid(row=23)
tk.Label(root, text="V").grid(row=24)
tk.Label(root, text="W").grid(row=25)
tk.Label(root, text="X").grid(row=26)
tk.Label(root, text="Y").grid(row=27)
tk.Label(root, text="Z").grid(row=28)

populate()

entry[28] = tk.Button(root, text='Load', command= lambda:populate()).grid(row=30,column=0)
entry[29] = tk.Button(root, text='Save', command= lambda:save_file()).grid(row=30,column=1)
entry[30] = tk.Button(root, text='Run', command= lambda:goldenapp()).grid(row=30,column=2)
entry[31] = tk.Button(root, text='Quit', command= root.quit).grid(row=30,column=3)

root.mainloop()




