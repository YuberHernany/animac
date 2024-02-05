from manim import *
import numpy as np 

class QueEsYComoGraficar(Scene):
    def construct(self):
        #pone funcion
        tex_ppal = MathTex("f(x) = \\frac{1}{16} x ^{2} + 1").scale(2).to_corner(DL)
        self.play(Write(tex_ppal))
        self.wait(1)
        def f(x):
            return (1/16)*x**2+1
        plano = NumberPlane()
        self.add(plano)
        nums = [k for k in range(-4,5)]
        res = [f(k) for k in nums]
        puntos = VGroup(*[Dot([k,0,0]) for k in nums])
        texs = MathTex(*[f"{k}" for k in nums])
        f_texs = MathTex(*[f"f({k})={np.round(r,1)}" for k,r in zip(nums, res)]).scale(0.5)
        for f_x in f_texs:
            f_x.next_to(tex_ppal, UP)
        for t, p in zip(texs, puntos):
            t.next_to(p, DOWN)
        self.play(Write(texs))
        self.wait(2)
        alturas = [0.7*(0 - k) for k in nums]
        for f_x, altura in zip(f_texs, alturas):
            self.play(FadeIn(f_x), run_time=0.1)
            self.play(f_x.animate.shift(9*RIGHT+altura*UP), run_time=0.1)
        self.play(Create(puntos))
        self.wait(1)
        # eleva puntos
        for r, p in zip(res, puntos):
            self.play(p.animate.shift(r*UP), run_time=0.1)
        curva = FunctionGraph(lambda x: f(x))
        self.play(Write(curva), run_time=4)
        self.wait(1)
        todo = VGroup(*[tex_ppal, plano, puntos, texs, f_texs, curva])
        self.play(FadeOut(todo))
        self.wait(1)

     #pone funcion otro ejemplo
        tex_ppal = MathTex("f(x) = \\frac{1}{8} x ^{3} -\\frac{1}{8} x + 1").scale(2).to_corner(DL)
        self.play(Write(tex_ppal))
        self.wait(1)
        def f(x):
            return (1/8)*x*(x-1)*(x+1)+1

        plano = NumberPlane()
        self.add(plano)
        nums = [k for k in range(-4,5)]
        res = [f(k) for k in nums]
        puntos = VGroup(*[Dot([k,0,0]) for k in nums])
        texs = MathTex(*[f"{k}" for k in nums])
        f_texs = MathTex(*[f"f({k})={np.round(r,1)}" for k,r in zip(nums, res)]).scale(0.5)
        for f_x in f_texs:
            f_x.next_to(tex_ppal, UP)
        for t, p in zip(texs, puntos):
            t.next_to(p, DOWN)
        self.play(Write(texs))
        self.wait(2)
        alturas = [0.7*(0 - k) for k in nums]
        for f_x, altura in zip(f_texs, alturas):
            self.play(FadeIn(f_x), run_time=0.1)
            self.play(f_x.animate.shift(7*RIGHT+altura*UP), run_time=0.1)
        self.play(Create(puntos))
        self.wait(1)
        # eleva puntos
        for r, p in zip(res, puntos):
            self.play(p.animate.shift(r*UP), run_time=0.1)
        curva = FunctionGraph(lambda x: f(x))
        self.play(Write(curva), run_time=4)
        self.wait(1)
        todo = VGroup(*[tex_ppal, plano, puntos, texs, f_texs, curva])
        self.play(FadeOut(todo))
        self.wait(1)

