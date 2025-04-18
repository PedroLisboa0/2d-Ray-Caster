from manim import *

class Raycaster(Scene):
    def construct(self):
        # Text
        title = Text("Ray Caster", font_size=48, color=BLUE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        lightsource_label = Text("Light Source", font_size=24, color=BLUE)

        # Create circle
        circle = Circle(radius=0.1, color=RED)
        self.play(Create(circle))
        self.play(circle.animate.shift(4 * LEFT))
        self.play(Write(lightsource_label), lightsource_label.animate.next_to(circle, DOWN, buff=0.8))


        # Draw Wall
        wall = Line(ORIGIN + np.array([0, -1, 0]) * 2, ORIGIN + np.array([0, 1, 0]) * 2, color=PURPLE, stroke_width=4)
        wall.center = ORIGIN
        self.play(Create(wall))
        self.play(wall.animate.shift(3*RIGHT))

        num_rays = 8
        angle_start = -PI / 6     # -30 degrees in radians
        angle_end = PI / 6        # +30 degrees in radians
        total_angle = angle_end - angle_start


        rays = VGroup()
        for i in range(num_rays):
            # Evenly space angles within arc
            angle = angle_start + i * (total_angle / (num_rays - 1))
            direction = np.array([np.cos(angle), np.sin(angle), 0])
            end_point = circle.get_center() + direction * 10
            ray = Line(circle.get_center(), end_point, color=WHITE, stroke_width=2)
            rays.add(ray)
            self.play(Create(ray), runtime=1)



        # Fade out everything minus one ray and the wall
        last_ray = rays[4]
        rays.remove(last_ray)
        self.play(FadeOut(circle, title, lightsource_label, rays))
        self.play(wall.animate.move_to(ORIGIN), last_ray.animate.shift(LEFT * 3))
        circle = Circle(0.3, color=RED)
        circle.move_to([0,0.5,0])
        circle.set_fill(RED, opacity=0.5)
        self.wait(2)
        self.play(Create(circle))
        self.wait(2)

        # Label collision point
        label = Text("Collision Point", font_size=24, color=RED)
        label.next_to(circle, LEFT+np.array([0, -0.2, 0]), buff=0.3)
        self.play(Create(label))
        self.wait(2)
