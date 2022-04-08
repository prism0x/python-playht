from manim import *
from playht import tts
import pygments.styles as code_styles

code_style = code_styles.get_style_by_name("monokai")


class VoiceoverDemo(Scene):
    def construct(self):
        banner = ManimBanner().scale(0.5)

        self.add_sound(tts("Hey Manim Community!"))
        self.play(
            banner.create(),
        )

        self.add_sound(
            tts(
                "Today, I want to show you how you can generate voiceovers directly in your Python code."
            )
        )
        self.play(
            banner.expand(),
        )
        self.wait(4)
        self.play(FadeOut(banner))

        demo_code = Code(
            code='''self.add_sound(
    tts(
        """AI generated voices have become realistic
        enough for use in most content. Using neural
        text-to-speech frees you from the painstaking
        process of recording and manually syncing
        audio to your video."""
    )
)
self.play(Write(demo_code), run_time=11.5)''',
            # tab_width=4,
            # background_stroke_width=1,
            # background_stroke_color=WHITE,
            insert_line_no=False,
            style=code_style,
            background="window",
            font="Consolas",
            language="python",
        ).rescale_to_fit(12, 0)

        self.add_sound(
            tts(
                """AI generated voices have become realistic
                enough for use in most content. Using neural
                text-to-speech frees you from the painstaking
                process of recording and manually syncing
                audio to your video."""
            )
        )
        self.play(Write(demo_code), run_time=11.5)

        self.add_sound(
            tts(
                """As you can see, Manim started playing this voiceover,
                right as the code object started to be drawn.
                Let's see some more examples."""
            )
        )
        self.wait(7)
        self.play(FadeOut(demo_code))

        circle = Circle()
        square = Square().shift(2 * RIGHT)
        self.add_sound(tts("This circle is drawn as I speak."))
        self.play(Create(circle))
        self.wait(2)

        self.add_sound(tts("Let's shift it to the left 2 units."))
        self.play(circle.animate.shift(2 * LEFT))
        self.wait(2)

        self.add_sound(tts("Now, let's transform it into a square."))
        self.play(Transform(circle, square))
        self.wait(2)

        self.add_sound(
            tts(
                """I would go on, but you get the idea. You can find this demo in the GitHub repo shown on your screen."""
            )
        )
        self.wait(3)
        self.play(FadeOut(circle))
        self.play(FadeIn(Tex("https://github.com/prism0x/python-playht")))

        self.wait(5)
