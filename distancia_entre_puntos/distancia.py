from manim import *

class DistanciaEntrePuntos(Scene):
    def construct(self):
        # crea dos puntos y crea triangulo y plano
        plano = NumberPlane(x_range=[-5.1, 11.1, 1], y_range=[-2,8,1])
        self.play(Create(plano))
        p1 = Dot([0,-1,0]).scale(2).set_color(YELLOW)
        p2 = Dot([4,2,0]).scale(2).set_color(YELLOW)
        self.play(FadeIn(p1, p2))
        hip = Line([0,-1,0],[4,2,0]).set_color(ORANGE)
        cat1 = Line([0,-1,0],[4,-1,0]).set_color(GRAY)
        cat2 = Line([4,-1,0],[4,2,0]).set_color(GRAY)
        self.play(Create(hip), run_time=3)
        self.wait(1)
        self.add(cat1, cat2)
        self.wait(3)

        #textos
        p1_c = MathTex("(","3",",","2",")").scale(2).next_to(p1, DOWN)
        #               0   1   2   3   4
        p2_c = MathTex("(","7",",","5",")").scale(2).next_to(p2, RIGHT)
        #               0   1   2   3   4        
        self.add(p1_c, p2_c)

        # reemplaza en formula de distancia
        formula = MathTex("\sqrt{", "(", "\\quad", "-", "\\quad", ")", "^{2}", "+", "(", "\\quad", "-", "\\quad", ")", "^{2}}")
        #                     0      1      2       3      4       5     6      7    8      9       10     11      12     13
        formula.scale(2).next_to(7.2*LEFT+2.7*UP)
        self.add(formula)

        #mover numeros
        self.play(p2_c[1].animate.next_to(formula[2]).shift(1.8*LEFT))
        self.play(p1_c[1].animate.next_to(formula[4]).shift(1.1*LEFT))
        self.play(p2_c[3].animate.next_to(formula[9]).shift(1.8*LEFT))
        self.play(p1_c[3].animate.next_to(formula[11]).shift(1.2*LEFT))
        self.play(FadeOut(p1_c[0:5:2]), FadeOut(p2_c[0:5:2]),
                  FadeOut(cat1, cat2))
        
        #desarrollo
        res1 = MathTex("\\sqrt{4^2+3^2}").scale(2).next_to(formula, DOWN)
        res2 = MathTex("\\sqrt{16+9}").scale(2).next_to(res1, DOWN)
        res3 = MathTex("\\sqrt{25}").scale(2).next_to(res2, DOWN)
        res4 = MathTex("5").scale(2).next_to(res3, DOWN)
        for cosa in [res1, res2, res3, res4]:
            self.play(Write(cosa))
        self.wait(1)
