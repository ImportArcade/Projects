
import arcade
import math
import random
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Asteroid Shoot-em Up"
LIFE_SCALE = 0.5

AREA_SIZE = 100
class GameOver(arcade.View):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("game_over.png")
    def on_draw(self):
        """
        Sets the size of game over screen
        """
        arcade.start_render()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH, SCREEN_HEIGHT)
    def on_key_press(self, key, key_modifiers):
        """
        When the space key is pressed, the game resets
        """
        if key == arcade.key.SPACE:
            game_view = MyGame()
            game_view.setup()
            self.window.show_view(game_view)

class YouWin(arcade.View):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("youwin.jpg")
    def on_draw(self):
        """
        Sets the size of the win screen
        """
        arcade.start_render()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH, SCREEN_HEIGHT)
        
        
class Player(arcade.Sprite):
    """
    Sprite that turns and moves
    """
    def __init__(self):
        super().__init__("ship_C.png")

        self.rotation = 0
        self.cur_pos_x = self.center_x
        self.cur_pos_y = self.center_y
        self.respawning = 0

        self.respawn()


    def LeftRightUpdate(self):
        """
        Function that rotates the ship when left and right keys are pressed.
        """
        self.angle += self.rotation
        
    def ForwardBackUpdate(self):
        """
        Function that moves the ship in the direction it is facing
        and backwards when up and down keys are pressed
        """
        angle_rad = math.radians(self.angle)
        self.center_x += -self.change_x * math.sin(angle_rad)
        self.center_y += self.change_y * math.cos(angle_rad)

        if self.center_x < 0:
            self.center_x = 0
        if self.center_x > SCREEN_WIDTH:
            self.center_x = SCREEN_WIDTH
        if self.center_y < 0:
            self.center_y = 0
        if self.center_y > SCREEN_HEIGHT:
            self.center_y = SCREEN_HEIGHT
    def respawn(self):
        self.respawning = 1
        self.center_x = SCREEN_WIDTH / 2
        self.center_y = SCREEN_HEIGHT / 2
        self.angle = 0
    def respawn_update(self):
         if self.respawning:
            self.respawning += 1
            self.alpha = self.respawning
            if self.respawning > 50:
                self.respawning = 0
                self.alpha = 255
    def on_update(self, delta_time: float = 1/60):
        self.LeftRightUpdate()
        self.ForwardBackUpdate()
        self.respawn_update()


class Asteroid(arcade.Sprite):
    def __init__(self):
        super().__init__("meteor_detailedLarge.png")

        self.change_x = 0
        self.change_y = 0

    def AsteroidMovement(self):
        """
        Movement function for asteroids
        """
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.center_x < 0:
            self.change_x *= -1
        if self.center_x > SCREEN_WIDTH:
            self.change_x *= -1
        if self.center_y< 0:
            self.change_y *= -1
        if self.center_y > SCREEN_HEIGHT:
            self.change_y *= -1
    def FreezeAsteroid(self):
        self.change_x = 0
        self.change_y = 0
    def on_update(self, delta_time: float = 1/60):
        self.AsteroidMovement()
class Laser(arcade.Sprite):
    def __init__(self):
        super().__init__("star_tiny.png")

        self.change_x = 0
        self.change_y = 0
    def LaserMovement(self):
        """
        Set up so the laser is shot in the direction
        the ship is pointing
        """
        angle_rad = math.radians(self.angle)
        self.center_x += -self.change_x * math.sin(angle_rad)
        self.center_y += self.change_y * math.cos(angle_rad)
    def on_update(self, delta_time: float = 1/60):
        self.LaserMovement()

class PowerUp(arcade.Sprite):
    def __init__(self):
        super().__init__("effect_purple.png")

class PlayerLife(arcade.Sprite):
    def __init__(self):
        super().__init__("ship_C.png",LIFE_SCALE)


                 


class MyGame(arcade.View):
    """
    Main application class.
    """

    def __init__(self):
        super().__init__()

        self.background = None

        arcade.set_background_color(arcade.color.BLACK)


        #Sprite Lists
        self.all_sprites_list = None
        self.asteroid_list = None
        self.player_sprite = None
        self.laser_list = None
        self.powerup_list = None
        self.life_list = None
        self.lives = 3

        #List of Sounds
        self.laser_shoot = arcade.load_sound("laserRetro_002.ogg")
        self.explosion = arcade.load_sound("explosionCrunch_004.ogg")
        self.game_over = arcade.load_sound("mixkit-arcade-space-shooter-dead-notification-272.wav")
        self.next_level = arcade.load_sound("jingles_NES03.ogg")
        self.win_game = arcade.load_sound("mixkit-video-game-win-2016.wav")
        self.life_lost = arcade.load_sound("jingles_NES15.ogg")
        self.powerup_get = arcade.load_sound("forceField_002.ogg")


    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        
        self.all_sprites_list = arcade.SpriteList()
        self.asteroid_list = arcade.SpriteList()
        self.laser_list = arcade.SpriteList()
        self.powerup_list = arcade.SpriteList()
        self.life_list = arcade.SpriteList()

        self.score = 0
        self.level = 1


        
        # Player list
        self.player_sprite = Player()
        self.player_sprite.center_x = 400
        self.player_sprite.center_y = 200
        self.player_sprite.angle = 0
        self.all_sprites_list.append(self.player_sprite)

        cur_pos = 650
        for i in range(self.lives):
            #PlayerLife list
            
            self.life_sprite = PlayerLife()
            self.life_sprite.center_x = cur_pos + self.life_sprite.width
            self.life_sprite.center_y = self.life_sprite.height
            cur_pos += self.life_sprite.width
            self.life_list.append(self.life_sprite)

        self.level_1()
        
        



    def level_1(self):
        """
        Sets up level 1
        """

        self.player_sprite.respawn()
        for i in range(random.randrange(2, 5)):


            buffer_x_high = self.player_sprite.cur_pos_x + AREA_SIZE
            buffer_x_low = self.player_sprite.cur_pos_x - AREA_SIZE
            buffer_y_high = self.player_sprite.cur_pos_y + AREA_SIZE
            buffer_y_low = self.player_sprite.cur_pos_y - AREA_SIZE
            #Asteroid list
            self.asteroid_sprite = Asteroid()
            self.asteroid_sprite.center_x = random.randrange(SCREEN_WIDTH)
            self.asteroid_sprite.center_y = random.randrange(SCREEN_HEIGHT)
            self.asteroid_sprite.change_x = random.randrange(-2, 3)
            self.asteroid_sprite.change_y = random.randrange(-2, 3)
            self.all_sprites_list.append(self.asteroid_sprite)
            self.asteroid_list.append(self.asteroid_sprite)
            if self.asteroid_sprite.center_x < buffer_x_high and self.asteroid_sprite.center_x > buffer_x_low and self.asteroid_sprite.center_y < buffer_y_high and self.asteroid_sprite.center_y > buffer_y_low:
                self.asteroid_sprite.center_x = random.randrange(SCREEN_WIDTH)
                self.asteroid_sprite.center_y = random.randrange(SCREEN_HEIGHT)
        #Power Up list
        self.powerup_sprite = PowerUp()
        
        if self.lives < 2:
            self.powerup_sprite.center_x = random.randrange(SCREEN_WIDTH)
            self.powerup_sprite.center_y = random.randrange(SCREEN_HEIGHT)
            self.powerup_list.append(self.powerup_sprite)
    def level_2(self):
        """
        Sets up level 2
        """
        self.player_sprite.respawn()
        buffer_x_high = self.player_sprite.cur_pos_x + AREA_SIZE
        buffer_x_low = self.player_sprite.cur_pos_x - AREA_SIZE
        buffer_y_high = self.player_sprite.cur_pos_y + AREA_SIZE
        buffer_y_low = self.player_sprite.cur_pos_y - AREA_SIZE
        for i in range(random.randrange(3,7)):
            #Asteroid list
            self.asteroid_sprite = Asteroid()
            self.asteroid_sprite.center_x = random.randrange(SCREEN_WIDTH)
            self.asteroid_sprite.center_y = random.randrange(SCREEN_HEIGHT)
            self.asteroid_sprite.change_x = random.randrange(-2, 3)
            self.asteroid_sprite.change_y = random.randrange(-2, 3)
            self.all_sprites_list.append(self.asteroid_sprite)
            self.asteroid_list.append(self.asteroid_sprite)
            if self.asteroid_sprite.center_x < buffer_x_high and self.asteroid_sprite.center_x > buffer_x_low and self.asteroid_sprite.center_y < buffer_y_high and self.asteroid_sprite.center_y > buffer_y_low:
                self.asteroid_sprite.center_x = random.randrange(SCREEN_WIDTH)
                self.asteroid_sprite.center_y = random.randrange(SCREEN_HEIGHT)

            
        #Power Up list
        self.powerup_sprite = PowerUp()
        if self.lives < 2:
            self.powerup_sprite.center_x = random.randrange(SCREEN_WIDTH)
            self.powerup_sprite.center_y = random.randrange(SCREEN_HEIGHT)
            self.powerup_list.append(self.powerup_sprite)
    def level_3(self):
        """
        Sets up level 3
        """
        self.player_sprite.respawn()
        buffer_x_high = self.player_sprite.cur_pos_x + AREA_SIZE
        buffer_x_low = self.player_sprite.cur_pos_x - AREA_SIZE
        buffer_y_high = self.player_sprite.cur_pos_y + AREA_SIZE
        buffer_y_low = self.player_sprite.cur_pos_y - AREA_SIZE
        for i in range(random.randrange(4,9)):
            self.asteroid_sprite = Asteroid()
            self.asteroid_sprite.center_x = random.randrange(SCREEN_WIDTH)
            self.asteroid_sprite.center_y = random.randrange(SCREEN_HEIGHT)
            self.asteroid_sprite.change_x = random.randrange(-3, 4)
            self.asteroid_sprite.change_y = random.randrange(-3, 4)
            self.all_sprites_list.append(self.asteroid_sprite)
            self.asteroid_list.append(self.asteroid_sprite)
            if self.asteroid_sprite.center_x < buffer_x_high and self.asteroid_sprite.center_x > buffer_x_low and self.asteroid_sprite.center_y < buffer_y_high and self.asteroid_sprite.center_y > buffer_y_low:
                self.asteroid_sprite.center_x = random.randrange(SCREEN_WIDTH)
                self.asteroid_sprite.center_y = random.randrange(SCREEN_HEIGHT)

        #Power Up list
        self.powerup_sprite = PowerUp()
        if self.lives < 2:
            self.powerup_sprite.center_x = random.randrange(SCREEN_WIDTH)
            self.powerup_sprite.center_y = random.randrange(SCREEN_HEIGHT)
            self.powerup_list.append(self.powerup_sprite)
    def level_4(self):
        """
        Sets up level 4
        """
        self.player_sprite.respawn()
        buffer_x_high = self.player_sprite.cur_pos_x + AREA_SIZE
        buffer_x_low = self.player_sprite.cur_pos_x - AREA_SIZE
        buffer_y_high = self.player_sprite.cur_pos_y + AREA_SIZE
        buffer_y_low = self.player_sprite.cur_pos_y - AREA_SIZE
        for i in range(random.randrange(5,10)):
            self.asteroid_sprite = Asteroid()
            self.asteroid_sprite.center_x = random.randrange(SCREEN_WIDTH)
            self.asteroid_sprite.center_y = random.randrange(SCREEN_HEIGHT)
            self.asteroid_sprite.change_x = random.randrange(-3, 4)
            self.asteroid_sprite.change_y = random.randrange(-3, 4)
            self.all_sprites_list.append(self.asteroid_sprite)
            self.asteroid_list.append(self.asteroid_sprite)
            if self.asteroid_sprite.center_x < buffer_x_high and self.asteroid_sprite.center_x > buffer_x_low and self.asteroid_sprite.center_y < buffer_y_high and self.asteroid_sprite.center_y > buffer_y_low:
                self.asteroid_sprite.center_x = random.randrange(SCREEN_WIDTH)
                self.asteroid_sprite.center_y = random.randrange(SCREEN_HEIGHT)

        #Power Up list
        self.powerup_sprite = PowerUp()

        if self.lives < 2:
            self.powerup_sprite.center_x = random.randrange(SCREEN_WIDTH)
            self.powerup_sprite.center_y = random.randrange(SCREEN_HEIGHT)
            self.powerup_list.append(self.powerup_sprite)

        

    def on_draw(self):
        """
        Render the screen.
        """

        arcade.start_render()


        # Call draw() on all your sprite lists below
        self.all_sprites_list.draw()
        self.asteroid_list.draw()
        self.laser_list.draw()
        self.life_list.draw()
        self.powerup_list.draw()

        arcade.draw_text(f"Score: {self.score}", 10, 20, arcade.color.WHITE, 14)
        arcade.draw_text(f"Level: {self.level}", 20, 40, arcade.color.WHITE, 14)

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.all_sprites_list.on_update(delta_time)
        self.asteroid_list.on_update(delta_time)
        self.laser_list.on_update(delta_time)
        if not self.player_sprite.respawning:
            player_collision_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                                self.asteroid_list)
            if len(player_collision_list) > 0:
                if self.lives > 0:
                    self.lives -= 1
                    self.player_sprite.respawn()
                    self.life_list.pop().remove_from_sprite_lists()
                    arcade.play_sound(self.life_lost)
                if self.lives == 0:
                    view = GameOver()
                    self.window.show_view(view)
                    arcade.play_sound(self.game_over)
            

        for laser in self.laser_list:
            hit_list = arcade.check_for_collision_with_list(laser, self.asteroid_list)
            if len(hit_list) > 0:
                laser.remove_from_sprite_lists()
            for asteroid in hit_list:
                asteroid.remove_from_sprite_lists()
                arcade.play_sound(self.explosion)
                self.score += 1

            if laser.bottom > SCREEN_HEIGHT or laser.bottom < 0:
                laser.remove_from_sprite_lists()
            if laser.bottom > SCREEN_WIDTH or laser.bottom < 0:
                laser.remove_from_sprite_lists()

        powerup_collision_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                                      self.powerup_list)
        for powerup in powerup_collision_list:
            for asteroid in self.asteroid_list:
                asteroid.FreezeAsteroid()
                arcade.play_sound(self.powerup_get)
                powerup.remove_from_sprite_lists()
                

        if len(self.asteroid_list) == 0 and self.level == 1:
            self.powerup_list = arcade.SpriteList()
            self.level += 1
            self.level_2()
            arcade.play_sound(self.next_level)
            time.sleep(1)
            
        if len(self.asteroid_list) == 0 and self.level == 2:
            self.powerup_list = arcade.SpriteList()
            self.level += 1
            self.level_3()
            arcade.play_sound(self.next_level)
            time.sleep(1)
        if len(self.asteroid_list) == 0 and self.level == 3:
            self.powerup_list = arcade.SpriteList()
            self.level += 1
            self.level_4()
            arcade.play_sound(self.next_level)
            time.sleep(1)
        if len(self.asteroid_list) == 0 and self.level == 4:
            view = YouWin()
            self.window.show_view(view)
            arcade.play_sound(self.win_game)

    
            

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.
        """
        if key == arcade.key.LEFT:
            self.player_sprite.rotation = 5
        if key == arcade.key.RIGHT:
            self.player_sprite.rotation = -5
        if key == arcade.key.UP:
            self.player_sprite.change_x = 5
            self.player_sprite.change_y = 5
        if key == arcade.key.DOWN:
            self.player_sprite.change_x = -5
            self.player_sprite.change_y = -5
        if key == arcade.key.SPACE:
            laser = Laser()
            laser.angle = self.player_sprite.angle
            laser.change_y = 10
            laser.change_x = 10
            laser.center_x = self.player_sprite.center_x
            laser.center_y = self.player_sprite.center_y
            self.laser_list.append(laser)

            arcade.play_sound(self.laser_shoot)
            
            

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.rotation = 0
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
            self.player_sprite.change_x = 0            


def main():
    """ Main function """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = MyGame()
    window.show_view(start_view)
    start_view.setup()
    arcade.run()


if __name__ == "__main__":
    main()
