import arcade


def main ():
    arcade.open_window(800, 800, "first window example")
    arcade.set_background_color(arcade.color.ALMOND)

    #now create objects
    main_house = arcade.create_rectangle(400, 200, 400, 400, arcade.color.ANTIQUE_BRASS)
    door= arcade.create_rectangle(400,75,100,150,arcade.color.ARMY_GREEN)
    window_1= arcade.create_ellipse(300,300,50,50,arcade.color.AERO_BLUE)
    window_2 = arcade.create_ellipse(500,300,50,50,arcade.color.AERO_BLUE)
    roof_points = [(200,400),(400,600),(600,400)]
    roof= arcade.create_polygon(roof_points, arcade.color.DARK_GRAY)
    line= arcade.create_line(200,730,510,730,arcade.color.ROSE)

    #now we will begin to draw
    arcade.start_render()
    #draw everything here
    arcade.draw_text("boy is that an ugly house" , 200, 750, arcade.color.ALABAMA_CRIMSON, 22)

    main_house.draw()
    door.draw()
    window_1.draw()
    window_2.draw()
    roof.draw()
    line.draw()







    arcade.finish_render()

    arcade.run()


main()
