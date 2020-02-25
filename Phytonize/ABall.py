#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np #, time
import matplotlib.pyplot as plt
import matplotlib.animation as anim




class Ball:

    #Constants and class shared

    g = 9.8

    def add(a, b):
        c = np.zeros(3, float)
        c[0] = a[0]+b[0]
        c[1] = a[1]+b[1]
        c[2] = a[2]+b[2]
        return(c)

    #class functions

    def __init__(self, r, v, m, R):
        self.r = np.array(r)
        self.v = np.array(v)
        self.m = m
        self.R = R
        self.f = np.array([0,0,-self.m*Ball.g])
        self.VR = [[], [], []]
       # self.VV = [[], [], []]
        
    #def Force(self): self.f = np.array([0,0,-self.m*Ball.g])

    def Move(self, dt):
        self.r = self.r + self.v*dt
        self.v = self.v + self.f*dt/self.m
        
    def Updating(self):
        self.VR[0].append(self.r[0])
        self.VR[1].append(self.r[1])
        self.VR[2].append(self.r[2])
        
    def Animation(self, x, y, filename):
        plt.close('All')
        
        fig = plt.figure(1)
        ax=plt.axes(xlim=(0,40),ylim=(-20,10))
        plt.grid(linestyle='-')
        plt.xlabel('x')
        plt.ylabel('z')
        
        [line]=ax.plot([],[], 'ro', lw=30*self.R)
        
        def init():
            line.set_data([],[])
            return([line])
        
        def animate(i):
            line.set_data([x[i-1]], [y[i-1]]) #(x[:i], y[:i])
            return([line]) 
        
        animation = anim.FuncAnimation(fig, animate, init_func=init,
                                       frames=len(x)+1,interval=1000, blit=True)
        animation.save(filename, writer=anim.PillowWriter(fps=10))
    

#if __name__=="__main__":

dt = 0.05
    #(r, v, m , R)
Body = Ball([0, 0, 0], [12, 0, 9], 1, 0.5)


for t in range(200):
    Body.Updating()
    Body.Move(dt)
Body.Animation(Body.VR[0], Body.VR[2], 'Animation.gif')