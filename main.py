def on_forever():
    if input.light_level() > 70:
        basic.show_leds("""
            # . # . #
            . # # # .
            # # # # #
            . # # # .
            # . # . #
            """)
        music.play(music.string_playable("E B C5 A B G A F ", 120),
            music.PlaybackMode.UNTIL_DONE)
    else:
        basic.clear_screen()
basic.forever(on_forever)
