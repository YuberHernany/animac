from manim import *
import numpy as np
import sympy as sy

class UnitarioYTriangPitag(Scene):
    def construct(self):
        eje_x_izq = NumberLine(x_range=[-4,0], length=4).shift(4*LEFT)
        eje_y_izq = NumberLine(x_range=[-4,0], length=4).rotate(90*DEGREES).shift(4*LEFT)
        unitario = Circle(radius=2, stroke_width=10).set_color(YELLOW).shift(4*LEFT)
        self.wait(1)
        coords = 2*np.array([[np.cos(2*k*np.pi/12), np.sin(2*k*np.pi/12), 0] for k in range(12)])
        def proy_x(arr):
            return np.array([arr[0], 0, 0])
        ori = np.array([0,0,0])
        triangs = VGroup(*[Polygon(*[ori, proy_x(row), row], stroke_width=10) for row in coords]).shift(5*LEFT).set_color(RED)
        mosaico_izq = VGroup(*[eje_x_izq, unitario, eje_y_izq]).shift(1*LEFT)
        self.add(mosaico_izq)
        for t in triangs:
            self.play(Transform(triangs[0], t), run_time=0.5)
        self.wait(2)

        axes = Axes(
            x_range=[-1, 13, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=14,
            axis_config={"color": GREEN}
        )
        axes_labels = axes.get_axis_labels()
        sin_graph = axes.plot(lambda x: np.sin(1.05*x), color=BLUE)
        marcas_tex = MathTex("1\\frac{\\pi}{3}", "2\\frac{\\pi}{3}", "3\\frac{\\pi}{3}", "4\\frac{\\pi}{3}", "5\\frac{\\pi}{3}", "6\\frac{\\pi}{3}",
                             "7\\frac{\\pi}{3}", "8\\frac{\\pi}{3}", "9\\frac{\\pi}{3}", "10\\frac{\\pi}{3}", "11\\frac{\\pi}{3}", "12\\frac{\\pi}{3}")
        marcas_tex.arrange(RIGHT, buff=1.4)
        marcas_tex.scale(0.5)
        marcas_tex.shift(0.5*DOWN+0.5*RIGHT)
        # self.add(marcas_tex)


        mosaico_der = VGroup(*[axes, sin_graph, marcas_tex])
        mosaico_der.shift(3*RIGHT)
        self.add(mosaico_der)
        self.wait(1)



