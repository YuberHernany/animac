from manim import *
import numpy as np

class Razones(Scene):
    def construct(self):
        def resaltar(obj):
            for _ in range(10):
                self.play(FadeIn(obj), run_time=0.2)
                self.play(FadeOut(obj), run_time=0.2)
        triangulo = Polygon(*[[4,0,0],[4,3,0],[0,0,0]], stroke_width=10)
        
        t_theta = MathTex("\\theta")
        t_theta.shift(1.3*RIGHT+0.5*UP).scale(2)
        
        arco = Arc(radius=2, stroke_width=10, start_angle=0, angle=TAU/10)

        
        self.wait(1)
        co1 = Line(4*RIGHT, 4*RIGHT+3*UP, stroke_width=15).set_color(YELLOW)
        # co2 = Line(4*RIGHT, 4*RIGHT+3*UP, stroke_width=15).set_color(YELLOW)
        
        hi1 = Line(ORIGIN, 4*RIGHT+3*UP, stroke_width=15).set_color(YELLOW)
        # hi2 = Line(ORIGIN, 4*RIGHT+3*UP, stroke_width=15).set_color(YELLOW)
        
        ca1 = Line(ORIGIN, 4*RIGHT, stroke_width=15).set_color(YELLOW)
        # ca2 = Line(ORIGIN, 4*RIGHT, stroke_width=15).set_color(YELLOW)
        
        mosaico_triang1 = VGroup(*[triangulo, t_theta, arco, co1, hi1, ca1])
        # mosaico_triang2 = VGroup(*[triangulo, t_theta, arco, co2, hi2, ca2])
        mosaico_triang1.scale(1.5).shift(2*DOWN)
        # mosaico_triang2.scale(1.5).shift(2*DOWN)
        self.play(Create(mosaico_triang1))
        
        t_co1 = Text("cateto opuesto").to_edge(UL)
        # t_co2 = Text("cateto opuesto").to_edge(UL)
        t_ca1 = Text("cateto adyacente").to_edge(UL)
        # t_ca2 = Text("cateto adyacente").to_edge(UL)
        linea_horizontal = Line(2*LEFT, 2*RIGHT, stroke_width=10).next_to(t_co1, DOWN)
        # linea_horizontal = Line(2*LEFT, 2*RIGHT, stroke_width=10).next_to(t_co2, DOWN)
        t_hi1 = Text('hipotenusa').next_to(linea_horizontal, DOWN)
        # t_hi2 = Text('hipotenusa').next_to(linea_horizontal, DOWN)
        razon_seno = VGroup(*[t_co1, linea_horizontal, t_hi1])
        # razon_coseno = VGroup(*[t_ca1, linea_horizontal, t_hi2])
        # razon_tangente = VGroup(*[t_co2, linea_horizontal, t_ca2])
        # self.add(razon_seno)
        t_sen = MathTex("\\sin (\\theta) = ").scale(2).to_edge(UL)
        t_cos = MathTex("\\cos (\\theta) = ").scale(2).to_edge(UL)
        t_tan = MathTex("\\tan (\\theta) = ").scale(2).to_edge(UL)
        razon_seno.next_to(t_sen, RIGHT)
        # razon_coseno.next_to(t_cos, RIGHT)
        # razon_tangente.next_to(t_tan, RIGHT)
        self.add(t_sen)
        self.wait(1)
        resaltar(co1)
        self.play(Transform(co1, t_co1))
        self.play(Create(linea_horizontal))
        resaltar(hi1)
        self.play(Transform(hi1, t_hi1))
        self.wait(1)

        todo = VGroup(*[mosaico_triang1, t_sen, t_co1, t_hi1, linea_horizontal, co1, hi1])
        self.play(FadeOut(todo))
        self.wait(1)

        triangulo = Polygon(*[[4,0,0],[4,3,0],[0,0,0]], stroke_width=10)

        t_theta = MathTex("\\theta")
        t_theta.shift(1.3*RIGHT+0.5*UP).scale(2)
        
        arco = Arc(radius=2, stroke_width=10, start_angle=0, angle=TAU/10)
        # co1 = Line(4*RIGHT, 4*RIGHT+3*UP, stroke_width=15).set_color(YELLOW)
        co2 = Line(4*RIGHT, 4*RIGHT+3*UP, stroke_width=15).set_color(YELLOW)
        
        # hi1 = Line(ORIGIN, 4*RIGHT+3*UP, stroke_width=15).set_color(YELLOW)
        hi2 = Line(ORIGIN, 4*RIGHT+3*UP, stroke_width=15).set_color(YELLOW)
        
        # ca1 = Line(ORIGIN, 4*RIGHT, stroke_width=15).set_color(YELLOW)
        ca2 = Line(ORIGIN, 4*RIGHT, stroke_width=15).set_color(YELLOW)
        
        # mosaico_triang1 = VGroup(*[triangulo, t_theta, arco, co1, hi1, ca1])
        mosaico_triang2 = VGroup(*[triangulo, t_theta, arco, co2, hi2, ca2])
        # mosaico_triang1.scale(1.5).shift(2*DOWN)
        mosaico_triang2.scale(1.5).shift(2*DOWN)
        self.play(Create(mosaico_triang2))
        
        # t_co1 = Text("cateto opuesto").to_edge(UL)
        t_co2 = Text("cateto opuesto").to_edge(UL)
        # t_ca1 = Text("cateto adyacente").to_edge(UL)
        t_ca2 = Text("cateto adyacente").to_edge(UL)
        linea_horizontal = Line(2*LEFT, 2*RIGHT, stroke_width=10).next_to(t_ca2, DOWN)
        # linea_horizontal = Line(2*LEFT, 2*RIGHT, stroke_width=10).next_to(t_co2, DOWN)
        # t_hi1 = Text('hipotenusa').next_to(linea_horizontal, DOWN)
        t_hi2 = Text('hipotenusa').next_to(linea_horizontal, DOWN)
        # razon_seno = VGroup(*[t_co1, linea_horizontal, t_hi1])
        razon_coseno = VGroup(*[t_ca1, linea_horizontal, t_hi2])
        # razon_tangente = VGroup(*[t_co2, linea_horizontal, t_ca2])
        # self.add(razon_seno)
        t_sen = MathTex("\\sin (\\theta) = ").scale(2).to_edge(UL)
        t_cos = MathTex("\\cos (\\theta) = ").scale(2).to_edge(UL)
        t_tan = MathTex("\\tan (\\theta) = ").scale(2).to_edge(UL)
        razon_coseno.next_to(t_cos, RIGHT)
        # razon_coseno.next_to(t_cos, RIGHT)
        # razon_tangente.next_to(t_tan, RIGHT)
        self.add(t_cos)
        self.wait(1)
        resaltar(ca1)
        self.play(Transform(ca1, t_ca1))
        self.play(Create(linea_horizontal))
        resaltar(hi2)
        self.play(Transform(hi2, t_hi2))
        self.wait(1)

        todo = VGroup(*[mosaico_triang2, t_cos, t_ca1, t_hi2, linea_horizontal, ca1, hi2])
        self.play(FadeOut(todo))
        self.wait(1)

