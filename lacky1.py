import arcade
import random
from arcade import gui
from arcade import gl
import time

WIDHT = 1200
HEIGHT = 800
SPEED = 7
GRAVITY = 1
JUMP = 25
VIEWPORT_MARGIN = 200
score = 0
life = 3
isGround = True
class StartView(arcade.View):
    def __init__(self):
        super().__init__()
        self.ui_manager = arcade.gui.UIManager()
        self.ui_manager1 = arcade.gui.UIManager()
        self.ui_manager2 = arcade.gui.UIManager()

        self.v_box = arcade.gui.UIBoxLayout()
        self.v_box1 = arcade.gui.UIBoxLayout()
        self.v_box2 = arcade.gui.UIBoxLayout()


        start_button = arcade.gui.UIFlatButton(text="START", width=200)
        self.v_box.add(start_button.with_space_around(bottom= 280))

        settings_button = arcade.gui.UIFlatButton(text='SETTINGS', width= 200)
        self.v_box1.add(settings_button.with_space_around(bottom= 150))

        quit_button = arcade.gui.UIFlatButton(text='QUIT', width=200)
        self.v_box2.add(quit_button.with_space_around(bottom=20))

        start_button.on_click = self.start_game
        settings_button.on_click = self.settings
        quit_button.on_click = arcade.exit()

        self.ui_manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)

        )
        self.ui_manager1.add(
            arcade.gui.UIAnchorWidget(anchor_x='center_x',
                                                       anchor_y='center_y',
                                                       child=self.v_box1)
                             )

        self.ui_manager2.add(
            arcade.gui.UIAnchorWidget(anchor_x='center_x',
                                      anchor_y='center_y',
                                      child=self.v_box2)
        )


    def start_game(self, _):
        game_view = GameWindow()
        game_view.setup()
        self.window.show_view(game_view)

    def settings(self, _):
        settings_view = Settings()
        settings_view.setup()
        self.window.show_view(settings_view)
    def quit(self):
        arcade.exit()


    def on_show(self): # эту фунцкцию мы запускаем при показе этого экрана
        arcade.set_background_color(arcade.color.BLUE)
        self.ui_manager.enable()
        self.ui_manager1.enable()
        self.ui_manager2.enable()

    def on_draw(self):
        arcade.start_render()
        self.ui_manager.draw()
        self.ui_manager1.draw()
        self.ui_manager2.draw()

    def on_hide_view(self):
        self.ui_manager.disable()
        self.ui_manager1.disable()
        self.ui_manager2.disable()

class Settings(arcade.View):
    def __init__(self):
        super().__init__()
        self.text = arcade.draw_text('Здесь и настраивать нечего :)', 100, HEIGHT // 2, arcade.color.WINE, 30)
    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text('Здесь и настраивать нечего :)', 100, HEIGHT // 2, arcade.color.WINE, 30)




    def setup(self):
        pass


class Tikva(arcade.Sprite):
    def __init__(self):
        super().__init__('resource/okrug/tikva.png')

class Peace(arcade.Sprite):
    def __init__(self):
        super().__init__('resource/okrug/peace.png')



class Player(arcade.Sprite):
    def __init__(self):
        super().__init__(':resources:images/animated_characters/female_person/femalePerson_idle.png')

class Life(arcade.Sprite):
    def __init__(self):
        super().__init__()

class Shipi(arcade.Sprite):
    def __init__(self):
        super().__init__('resource/okrug/shipi.png', 2)
class Ground(arcade.Sprite):
    def __init__(self):
        super().__init__('resource/okrug/ground1.png')

class GameWindow(arcade.View):
    def __init__(self):
        super().__init__()

        self.peace_list = None
        self.peace_list1 = None
        self.background = arcade.load_texture('resource/okrug/background.png')
        self.music =arcade.sound.load_sound('music.mp3')
        self.sound = arcade.sound.load_sound('sqek.mp3')
        self.sound2 = arcade.sound.load_sound('damage.mp3')

        self.media_player = self.music.play(0.5, loop=True)
        self.isGround = True
        self.ground_list = None
        self.player = None
        self.physics_engine = None
        self.item_list = None
        self.shipi_list = None
        self.life1 = arcade.load_texture('resource/okrug/heart1.png')
        self.life2 = arcade.load_texture('resource/okrug/heart2.png')
        self.life3 = arcade.load_texture('resource/okrug/heart3.png')
        self.life4 = arcade.load_texture('resource/okrug/heart4.png')




    def menu(self ):
        """Закончить игру сообщением"""
        start_view = GameWindow()
        self.window.show_view(start_view)
        arcade.sound.stop_sound(self.media_player)


    def setup(self):
        self.shipi_list = arcade.SpriteList()
        self.ground_list = arcade.SpriteList()
        self.item_list = arcade.SpriteList()
        self.life_list = arcade.SpriteList()
        self.peace_list = arcade.SpriteList()
        self.peace_list1 = arcade.SpriteList()

        for j in range(0, 900, 64):
            ground1 = Ground()
            ground1.center_x = 1
            ground1.center_y = j
            self.ground_list.append(ground1)
        for i in range(0, 1300, 64):
            r_spite = random.randint(1, 2)
            ground = arcade.Sprite(f'resource/okrug/ground{r_spite}.png')
            ground.center_x = i
            ground.center_y = 20
            self.ground_list.append(ground)

        for a in range(64, 250, 64):
            r_spite = random.randint(1, 2)
            ground2 = arcade.Sprite(f'resource/okrug/ground{r_spite}.png')
            ground2.center_x = a
            ground2.center_y = 300
            self.ground_list.append(ground2)

        for b in range(350, 800, 64):
            r_spite = random.randint(1, 2)
            ground3 = arcade.Sprite(f'resource/okrug/ground{r_spite}.png')
            ground3.center_x = b
            ground3.center_y = 500
            self.ground_list.append(ground3)




        tikva = Tikva()
        tikva.center_x = 234
        tikva.center_y = 65
        self.item_list.append(tikva)
        tikva1 = Tikva()
        tikva1.center_x = 570
        tikva1.center_y = 564
        self.item_list.append(tikva1)
        tikva2 = Tikva()
        tikva2.center_x = 570
        tikva2.center_y = 64
        self.item_list.append(tikva2)
        tikva3 = Tikva()
        tikva3.center_x = 90
        tikva3.center_y = 564
        self.item_list.append(tikva3)
        tikva4 = Tikva()
        tikva4.center_x = 180
        tikva4.center_y = 364
        self.item_list.append(tikva4)

        shipi = Shipi()
        shipi.center_x = 400
        shipi.center_y = 70
        self.shipi_list.append(shipi)
        shipi1 = Shipi()
        shipi1.center_x = 500
        shipi1.center_y = 564
        self.shipi_list.append(shipi1)
        shipi2 = Shipi()
        shipi2.center_x = 76
        shipi2.center_y = 364
        self.shipi_list.append(shipi2)
        shipi = Shipi()
        shipi.center_x = 1000
        shipi.center_y = 70
        self.shipi_list.append(shipi)

        peace = Peace()
        peace.center_x = random.randint(70, 1100)
        peace.center_y = 64
        self.peace_list.append(peace)
        self.peace_list1.append(peace)
        peace1 = Peace()
        peace1.center_x = random.randint(70, 1100)
        peace1.center_y = 64
        self.peace_list.append(peace1)
        self.peace_list1.append(peace1)
        peace2 = Peace()
        peace2.center_x = random.randint(70, 1100)
        peace2.center_y = 64
        self.peace_list.append(peace2)
        self.peace_list1.append(peace2)
        peace3 = Peace()
        peace3.center_x = random.randint(70, 1100)
        peace3.center_y = 64
        self.peace_list.append(peace3)
        self.peace_list1.append(peace3)
        peace4 = Peace()
        peace4.center_x = random.randint(70, 1100)
        peace4.center_y = 64
        self.peace_list.append(peace4)
        self.peace_list1.append(peace4)




        self.player = Player()
        self.player.center_x = 70
        self.player.bottom = self.ground_list[0].top



        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player, gravity_constant=GRAVITY, walls=self.ground_list
        )


    def on_update(self, delta_time):
        global score
        global life
        self.physics_engine.update()
        self.player.update_animation()
        self.peace_list.update()
        self.menu()
        for shipi in self.shipi_list:
            s_list = arcade.check_for_collision(shipi, self.player)
            if s_list:

                score -= 5
                life -= 1
                self.sound2.play()

                shipi.kill()


        for tikva in self.item_list:

            shot_list = arcade.check_for_collision(tikva, self.player)
            if shot_list:
                score += 10
                self.sound.play()

                tikva.kill()
        for p in self.peace_list:

            shot_list = arcade.check_for_collision(p, self.player)
            if shot_list:
                score += 1
                self.sound.play()
                p.kill()
        for p1 in self.peace_list1:

            shot_list1 = arcade.check_for_collision(p1, self.player)
            if shot_list1:
                score += 1
                self.sound.play()
                p1.kill()


    def on_draw(self):
        self.clear()
        arcade.start_render()
        self.background.draw_sized(600, 400, 1200, 800)
        self.ground_list.draw()
        self.player.draw()
        self.item_list.draw()
        self.shipi_list.draw()

        if life == 3:
            self.life1.draw_sized(128, 720, 256, 64 )

        elif life == 2:
            self.life2.draw_sized(128, 720, 256, 64)
            self.peace_list.draw()
        elif life == 1:
            self.life3.draw_sized(128, 720, 256, 64)
            self.peace_list1.draw()
        elif life <= 0:
            self.life4.draw_sized(128, 720, 256, 64)

            arcade.draw_text('Игра окончена',128, 400, arcade.color.RED, 90)
            self.media_player.pause()



        arcade.draw_text(f'Score:{score}', 900, 700, (255, 0, 0), 35, font_name='comic sans ms')
        arcade.draw_text('P - поставить музыку на паузу, O - продолжить прослушивание', 10, 25, (0, 0, 0), 20, font_name='comic sans ms')




    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.W or key == arcade.key.SPACE:
            self.player.change_y = JUMP
            self.isGround = False
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player.change_x = -SPEED
            self.isGround = True
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player.change_x = SPEED
        elif key == arcade.key.P:
            self.media_player.pause()
        elif key == arcade.key.O:
            self.media_player.play()
        elif key == arcade.key.ESCAPE:
            self.menu()




    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player.change_x = 0


        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player.change_x = 0



if __name__ == '__main__':
    window = arcade.Window(WIDHT, HEIGHT, 'GG')
    start_view = StartView()
    window.show_view(start_view)
    arcade.run()