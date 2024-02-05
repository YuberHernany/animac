from manim import *

class Resuelve(Scene):
    def construct(self):
        eq1 = MathTex("5", " - ", "2 x", " = ", "7", " - ", "4x").scale(2)
        eq2 = eq1.copy().shift(UP)
        for ter in eq1:
            self.play(Write(ter))
        self.wait(3)
        self.play(eq1.animate.shift(3*UP))
        self.add_sound("sp1.mp3")
        self.wait(0.5)
        self.add(eq2)
        self.wait(3)
        self.play(Swap(*[eq2[0], eq2[6]]))
        self.add_sound("sp2.mp3")
        self.wait(3)
        eq3 = MathTex("2", "x",  "=", "2").scale(2).shift(0.5* DOWN)
        self.play(Write(eq3))
        self.wait(3)
        uno_hide = MathTex("1").next_to(eq3[3], 1.5*DOWN)
        hline = MathTex("\over").scale(2).next_to(eq3[3], DOWN).shift(0.2*UP)
        self.play(Write(hline))
        self.add_sound("sp3.mp3")
        self.play(eq3[0].animate.move_to(uno_hide))
        self.wait(3)
        eq4 = MathTex("x=1").scale(2).shift(2.5*DOWN)
        self.play(Write(eq4))
        self.wait(3)


class ResuelveTerna(Scene):
    def construct(self):
        eq1 = MathTex("{{a}}^2", "+", "{{b}}^2", "=", "{{c}}^2").scale(4)
        eq2 = MathTex("{{3}}^2", "+", "{{4}}^2", "=", "{{c}}^2").scale(4).shift(UP)
        eq3 = MathTex("9", "+", "16", "=", "{{c}}^2").scale(4)
        eq4 = MathTex("25", "=", "{{c}}^2").scale(4).shift(UP)
        eq5 = MathTex("\sqrt{25}", "=", "\sqrt{{{c}}^2}").scale(4)
        eq6 = MathTex("5", "=", "c").scale(4).shift(UP)

        self.add(eq1)
        self.wait(2)
        self.play(TransformMatchingTex(eq1, eq2))
        self.wait(1)
        self.play(TransformMatchingTex(eq2, eq3))
        self.wait(1)
        self.play(TransformMatchingTex(eq3, eq4))
        self.wait(1)
        self.play(TransformMatchingTex(eq4, eq5))
        self.wait(1)
        self.play(TransformMatchingTex(eq5, eq6))
        self.wait(1)


class ResuelveTernaCateto(Scene):
    def construct(self):
        eq1 = MathTex("{{a}}^2", "+", "{{b}}^2", "=", "{{c}}^2").scale(4)
        eq2 = MathTex("{{3}}^2", "+", "{{b}}^2", "=", "{{5}}^2").scale(4).shift(UP)
        eq3 = MathTex("{{b}}^2", "=", "{{5}}^2", "-", "{{3}}^2").scale(4)
        eq4 = MathTex("{{b}}^2", "=", "25", "-", "9").scale(4).shift(UP)
        eq5 = MathTex("{{b}}^2", "=", "16").scale(4)
        eq6 = MathTex("\sqrt{{{b}}^2}", "=", "\sqrt{16}").scale(4).shift(UP)
        eq7 = MathTex("b", "=", "4").scale(4)
        

        self.add(eq1)
        self.wait(2)
        self.play(TransformMatchingTex(eq1, eq2))
        self.wait(1)
        self.play(TransformMatchingTex(eq2, eq3))
        self.wait(1)
        self.play(TransformMatchingTex(eq3, eq4))
        self.wait(1)
        self.play(TransformMatchingTex(eq4, eq5))
        self.wait(1)
        self.play(TransformMatchingTex(eq5, eq6))
        self.wait(1)
        self.play(TransformMatchingTex(eq6, eq7))
        self.wait(1)

class TeoPita(Scene):
    def construct(self):
        T = Polygon([0,4,0], [0,0,0], [2,0,0])
        a_sq = Polygon([0,-2,0],[2,-2,0],[2,0,0],[0,0,0]).set_color(RED)
        a_sq.set_fill(RED, 1.0)
        b_sq = Polygon([0,0,0], [0,4,0], [-4,4,0],[-4,0,0]).set_color(BLUE)
        b_sq.set_fill(BLUE, 1.0)
        c_sq = Polygon([2,0,0], [0,4,0],[4,6,0], [6,2,0]).set_color(YELLOW)
        c_sq.set_fill(YELLOW, 1.0)
        t1 = Polygon([2,0,0],[2,4,0],[0,4,0])
        t1.set_fill(GREEN, 1.0)
        t2 = Polygon([6,2,0],[2,2,0],[2,0,0])
        t2.set_fill(GREEN, 1.0)
        t3 = Polygon([4,6,0],[4,2,0],[6,2,0])
        t3.set_fill(GREEN, 1.0)
        t4 = Polygon([0,4,0],[4,4,0],[4,6,0])
        t4.set_fill(GREEN, 1.0)
        s = Polygon([2,2,0],[4,2,0],[4,4,0],[2,4,0])
        s.set_fill(GREEN, 1.0)
        tt1 = Polygon([-2,0,0],[-2,4,0],[-4,4,0])
        tt1.set_fill(GREEN, 1.0)
        tt2 = Polygon([-4,4,0],[-4,0,0],[-2,0,0])
        tt2.set_fill(GREEN, 1.0)
        tt3 = Polygon([-2,4,0],[-2,0,0],[0,0,0])
        tt3.set_fill(GREEN, 1.0)
        tt4 = Polygon([0,0,0],[0,4,0],[-2,4,0])
        tt4.set_fill(GREEN, 1.0)
        ss = Polygon([0,-2,0],[2,-2,0],[2,0,0],[0,0,0])
        ss.set_fill(GREEN, 1.0)
        Todo = VGroup(a_sq, b_sq, c_sq, T, t1, t2, t3, t4, s, tt1, tt2, tt3, tt4, ss).shift(2*LEFT+2*DOWN).scale(0.9)
        # self.add(Todo)
        inicio = VGroup(T, a_sq, b_sq, c_sq)
        cubierta_sobre_c_sq = VGroup(t1,t2,t3,t4,s)
        cubierta_sobre_sqs_catetos = VGroup(tt1,tt2,tt3,tt4,ss)
        self.add_sound("teoPita.mp3")
        self.play(Create(inicio), run_time=8)
        self.wait(4)
        self.play(Create(cubierta_sobre_c_sq), run_time=7)
        self.wait(3)
        self.play(Transform(cubierta_sobre_c_sq, cubierta_sobre_sqs_catetos, path_arc=90*DEGREES, run_time=6))
        self.wait(3)

class EcuacionTeoPita(Scene):
    def construct(self):
        T = Polygon([0,4,0], [0,0,0], [2,0,0])
        a_sq = Polygon([0,-2,0],[2,-2,0],[2,0,0],[0,0,0]).set_color(RED)
        a_sq.set_fill(RED, 1.0)
        b_sq = Polygon([0,0,0], [0,4,0], [-4,4,0],[-4,0,0]).set_color(BLUE)
        b_sq.set_fill(BLUE, 1.0)
        c_sq = Polygon([2,0,0], [0,4,0],[4,6,0], [6,2,0]).set_color(YELLOW)
        c_sq.set_fill(YELLOW, 1.0)
        Todo = VGroup(a_sq, b_sq, c_sq, T).shift(2*LEFT+2*DOWN).scale(0.9)
        self.add(Todo)
        a = MathTex("a^2").scale(3).set_color(BLACK).move_to(a_sq)
        b = MathTex("b^2").scale(3).set_color(BLACK).move_to(b_sq)
        c = MathTex("c^2").scale(3).set_color(BLACK).move_to(c_sq)
        self.play(Create(a))
        self.play(Create(b))
        self.play(Create(c))
        eq = MathTex("a^2", "+", "b^2", "=", "c^2").scale(2).shift(4*RIGHT+3*DOWN)
        self.play(Write(eq), run_time=4)
        self.play(Transform(a, eq[0]))
        self.play(Transform(b, eq[2]))
        self.play(Transform(c, eq[4]))
        self.wait(1)

class NotacionEnAlgebra(Scene):
    def construct(self):
        # sobre notacion de exponente
        tex1 = MathTex("a \cdot a  =  a ^ 2").scale(3).shift(2.5*UP)
        tex2 = MathTex("a \cdot a \cdot a  =  a ^ 3").scale(3).shift(1.25*UP)
        tex3 = MathTex("a \cdot a \cdot a \cdot a =  a ^ 4").scale(3).shift(0.5*DOWN)
        tex4 = MathTex("a \cdot a \cdot a \cdot a \cdot a =  a ^ 5").scale(3).shift(2*DOWN)
        # self.add(tex1, tex2, tex3, tex4)
        primer_grupo = VGroup(*[tex1, tex2, tex3, tex4])
        # self.play(FadeOut(primer_grupo), run_time=2)

        # primera regla de potenciacion
        tex5 = MathTex("a^","2", " \cdot a^", "3", " = a^", "{2+3}", " = a^", "5").scale(3).shift(3*UP)
        # 1, 3, 5, 7
        self.play(Create(tex5))
        self.wait(1)
        caja1 = SurroundingRectangle(tex5[1])
        caja3 = SurroundingRectangle(tex5[3])
        caja5 = SurroundingRectangle(tex5[5])
        caja7 = SurroundingRectangle(tex5[7])
        for c in [caja1, caja3]:
            self.play(Create(c))
        paso1 = VGroup(*[caja1, caja3])
        self.play(Transform(paso1, caja5))
        self.wait(2)
        self.play(Transform(paso1, caja7))
        self.wait(1)
        text6 = MathTex("a \cdot a", "\cdot a \cdot a \cdot a", "=", "a^5").scale(3).shift(1.5*UP)
        self.play(Write(text6))
        self.wait(1)
        text7 = tex5[:2].copy()
        text8 = tex5[2:4].copy()
        self.play(Transform(text7, text6[0]))
        self.play(Transform(text8, text6[1]))
        self.wait(1)
        self.play(FadeOut(text6, text7, text8))
        self.wait(1)
        # otro ejemplo
        # primera regla de potenciacion
        tex5 = MathTex("a^","4", " \cdot a^", "6", " = a^", "{4+6}", " = a^", "{10}").scale(3).shift(UP)
        # 1, 3, 5, 7
        self.play(Create(tex5))
        self.wait(1)
        caja1 = SurroundingRectangle(tex5[1])
        caja3 = SurroundingRectangle(tex5[3])
        caja5 = SurroundingRectangle(tex5[5])
        caja7 = SurroundingRectangle(tex5[7])
        for c in [caja1, caja3]:
            self.play(Create(c))
        paso1 = VGroup(*[caja1, caja3])
        self.play(Transform(paso1, caja5))
        self.wait(2)
        self.play(Transform(paso1, caja7))
        self.wait(1)

        tex5 = MathTex("a^","6", " \cdot a^", "3", " = a^", "{6+3}", " = a^", "{9}").scale(3).shift(DOWN)
        # 1, 3, 5, 7
        self.play(Create(tex5))
        self.wait(1)
        caja1 = SurroundingRectangle(tex5[1])
        caja3 = SurroundingRectangle(tex5[3])
        caja5 = SurroundingRectangle(tex5[5])
        caja7 = SurroundingRectangle(tex5[7])
        for c in [caja1, caja3]:
            self.play(Create(c))
        paso1 = VGroup(*[caja1, caja3])
        self.play(Transform(paso1, caja5))
        self.wait(2)
        self.play(Transform(paso1, caja7))
        self.wait(1)

class CocienteDePotencias(Scene):
    def construct(self):
        self.add_sound('c.mp3')
        t1 = MathTex("x^", "{5}", "\over").scale(3).shift(2*UP+3*LEFT)
        t1s = MathTex("x^", "{3}").scale(3).next_to(t1, DOWN)
        caja1 = SurroundingRectangle(t1[1])
        caja2 = SurroundingRectangle(t1s[1])
        t2 = MathTex("=", "x^", "{5-3}").scale(3).next_to(t1, RIGHT)
        caja3 = SurroundingRectangle(t2[2])
        t3 = MathTex("=", "x^", "{2}").scale(3).next_to(t2, RIGHT)
        caja4 = SurroundingRectangle(t3[2])
        self.add(t1, t2, t3, t1s)
        self.add(caja1, caja2)
        self.wait(1)
        self.play(Transform(VGroup(*[caja1, caja2]), caja3))
        self.wait(2)
        self.play(Transform(VGroup(*[caja1, caja2]), caja4))
        self.wait(2)
        todo = VGroup(*[t1, t1s, caja1, caja2, t2, caja3, t3, caja4])
        self.play(FadeOut(todo))
        self.wait(2)

        #otro ejemplo
        t1 = MathTex("x^", "{7}", "\over").scale(3).shift(2*UP+3*LEFT)
        t1s = MathTex("x^", "{2}").scale(3).next_to(t1, DOWN)
        caja1 = SurroundingRectangle(t1[1])
        caja2 = SurroundingRectangle(t1s[1])
        t2 = MathTex("=", "x^", "{7-2}").scale(3).next_to(t1, RIGHT)
        caja3 = SurroundingRectangle(t2[2])
        t3 = MathTex("=", "x^", "{5}").scale(3).next_to(t2, RIGHT)
        caja4 = SurroundingRectangle(t3[2])
        self.add(t1, t2, t3, t1s)
        self.add(caja1, caja2)
        self.wait(1)
        self.play(Transform(VGroup(*[caja1, caja2]), caja3))
        self.wait(2)
        self.play(Transform(VGroup(*[caja1, caja2]), caja4))
        self.wait(2)
        todo = VGroup(*[t1, t1s, caja1, caja2, t2, caja3, t3, caja4])
        self.play(FadeOut(todo))
        self.wait(1)


class ClasificaAngulo(Scene):
    # en drive es mejor gestionar versiones y subir una nueva version
    def construct(self):
        l1 = Line(4*LEFT, 4*RIGHT)
        l2 = Line(3*DOWN + 4*LEFT, 3*UP + 4*RIGHT)
        self.add(l1, l2)
        angle1 = Angle(l1, l2, radius=2)
        angle2 = Angle(l1, l2, radius=2, quadrant=(-1,1))
        angle1_name = MathTex("45^{\circ}").shift(RIGHT*1.5+UP*0.5)
        self.add(angle1, angle1_name, angle2)
        self.wait(1)