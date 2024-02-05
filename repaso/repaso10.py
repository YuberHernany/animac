from manim import *
import numpy as np

class EscaIsosEqui(Scene):
    def construct(self):
    #     p_esca = [[0,0,0], [4,0,0], [0,3,0]]
    #     escaleno = Polygon(*p_esca).scale(1.7).shift(2*LEFT + 1.5*DOWN)
    #     t1 = Tex(r"$4 \ cm$")
    #     t2 = Tex(r"$3 \ cm$")
    #     t3 = Tex(r"$5 \ cm$")
    #     text_desc = Text("Escaleno").set_color(YELLOW).scale(2).shift(3*RIGHT + 2*UP)
    #     br1 = Brace(escaleno).set_color(YELLOW)
    #     br2 = Brace(escaleno).set_color(YELLOW)
    #     br2.next_to(escaleno, LEFT).scale(3/4)
    #     br2.rotate(270*DEGREES).shift(3.3*RIGHT)
    #     br3 = Brace(escaleno).set_color(YELLOW)
    #     br3.next_to(escaleno, UP)
    #     br3.rotate(-37*DEGREES).scale(5/4).shift(2.5*DOWN)
    #     t1.next_to(br1, DOWN)
    #     t2.next_to(br2, LEFT)
    #     t3.next_to(br3, UP).shift(2.4*DOWN)
    #     # self.add(escaleno, br1, br2, br3, t1, t2, t3, text_desc)
    #     self.play(Create(escaleno))
    #     self.wait(2)
    #     for t, b in zip([t1,t2,t3], [br1,br2,br3]):
    #         self.play(Create(t))
    #         self.play(Create(b))
    #         self.wait(1)
    #     self.play(Create(text_desc))
    #     self.wait(3)

        # ahora isosceles
        self.add_sound("isos.mp3")
        p_isos = [[5,0,0], [-5,0,0], [0,np.sqrt(11),0]]
        isosceles = Polygon(*p_isos).scale(1.3).shift(1.5*DOWN)
        t1 = Tex(r"$10 \ cm$")
        t2 = Tex(r"$6 \ cm$")
        t3 = Tex(r"$6 \ cm$")
        text_desc = Text("Isósceles").set_color(YELLOW).scale(2).shift(DOWN)
        br1 = Brace(isosceles).set_color(YELLOW)
        br2 = Brace(isosceles).set_color(YELLOW)
        br3 = Brace(isosceles).set_color(YELLOW)
        br2.scale(6/10).rotate(147*DEGREES).shift(3*UP + 3.5*RIGHT)
        br3.scale(6/10).rotate(33*DEGREES).shift(3*UP + 3.5*LEFT)
        t1.next_to(br1, DOWN)
        t2.next_to(br2, UP).shift(2*DOWN)
        t3.next_to(br3, UP).shift(2*DOWN)
        # self.add(isosceles, br1, br2, br3, t1, t2, t3, text_desc)
        self.play(Create(isosceles))
        self.wait(2)
        for t, b in zip([t1,t2,t3], [br1,br2,br3]):
            self.play(Create(t))
            self.play(Create(b))
            self.wait(1)
        self.play(Create(text_desc))
        self.wait(2)