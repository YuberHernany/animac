from manim import *
import numpy as np

def unitary_roots_coords(n):
    return np.array([[np.cos(2*k*np.pi/n), np.sin(2*k*np.pi/n), 0] for k in range(n)])


def unitary_roots_coords_scaled(n, radius):
    return unitary_roots_coords(n) * radius


def curve_coords(n):
    return 3*np.array([[np.sin(k/64) * np.cos(2*k*np.pi/n), 
                      np.sin(k/64) * np.sin(2*k*np.pi/n), 0] for k in range(n)])


class Circunferencia(Scene):
    def construct(self):
        # plano = NumberPlane()
        # self.add(plano)
        cir = Circle(radius=2, stroke_width=10).set_color(RED)
        self.add(cir)
        p_movil = Dot([cir.radius, 0, 0]).scale(1.3).set_color(YELLOW)
        radio_movil = Line(ORIGIN, cir.radius*RIGHT, stroke_width=10).set_color(YELLOW)
        self.wait(1)
        self.add(p_movil, radio_movil)
        self.wait(1)
        arr_coords = unitary_roots_coords_scaled(32, 2)
        puntos = VGroup(*[Dot(fila) for fila in arr_coords])
        self.add(puntos)
        self.wait(1)
        radios = VGroup(*[Line(ORIGIN, fila) for fila in arr_coords])
        self.add(radios)
        self.wait(1)
        self.play(Rotate(radio_movil, angle=2*PI/32, about_point=ORIGIN))
        self.wait(1)
        self.play(Rotate(radio_movil, angle=2*PI/32, about_point=ORIGIN))
        self.wait(1)
        self.play(Rotate(radio_movil, angle=2*PI/32, about_point=ORIGIN))
        self.wait(1)
        self.play(Rotate(radio_movil, angle=2*PI, about_point=ORIGIN, run_time=4))
        self.wait(1)
        self.play(FadeOut(radios, puntos, p_movil, radio_movil))
        self.wait(1)
        arr_coords_all = unitary_roots_coords_scaled(64, 2)
        puntos_all = VGroup(*[Dot(fila) for fila in arr_coords_all]).set_color(RED)
        self.play(Rotate(puntos_all, about_point=ORIGIN, angle=2*PI, run_time=5))
        self.wait(1)
        self.play(FadeOut(puntos_all))
        self.wait(1)
        self.play(FadeOut(cir))
        # cosa que no es circunferencia
        ir_coords = curve_coords(128)
        irregular_curve = Polygon(*ir_coords).set_color(YELLOW)
        radio1 = Line(ORIGIN, ir_coords[16], stroke_width=10).set_color(RED)
        radio2 = Line(ORIGIN, ir_coords[32], stroke_width=10).set_color(RED)
        radio3 = Line(ORIGIN, ir_coords[64], stroke_width=10).set_color(RED)
        radio4 = Line(ORIGIN, ir_coords[100], stroke_width=10).set_color(RED)
        self.play(Create(irregular_curve))
        self.play(Transform(radio1, radio2))
        self.play(Transform(radio2, radio3))
        self.play(Transform(radio3, radio4))
        self.wait(1)
        self.play(FadeOut(irregular_curve, radio1, radio2, radio3, radio4))
        self.wait(1)
        self.play(FadeIn(cir, radios))
        self.play(Rotate(radios, about_point=ORIGIN, angle=PI/8, run_time=3))
        self.wait(1)
        self.play(cir.animate.shift(3*LEFT), radios.animate.shift(3*LEFT))
        self.wait(1)
        self.play(cir.animate.scale(0.5), radios.animate.scale(0.5))
        self.wait(1)
        self.play(Rotate(radios, about_point=3*LEFT, angle=PI/8, run_time=3))
        self.wait(1)
        self.play(cir.animate.shift(5*RIGHT), radios.animate.shift(5*RIGHT))
        self.wait(1)
        self.play(cir.animate.scale(4), radios.animate.scale(4))
        self.wait(1)
        self.play(Rotate(radios, about_point=2*RIGHT, angle=PI/8, run_time=3))
        self.wait(1)

