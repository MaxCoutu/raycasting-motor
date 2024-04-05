# 🚀 Raycasting Motor

Welcome to the **Raycasting Motor** project! This project is a raycasting engine implemented in Python. It includes the basic operations of the engine and also supports texture display during 3D rendering. We are currently developing a game that uses this engine to navigate through a randomly generated maze.

## 🎮 How It Works

The raycasting engine works by casting rays from the player's position into the scene to detect walls. Each ray represents a vertical slice of the scene, and the distance from the player to the wall for each ray is used to calculate the height of the wall slice on the screen. This creates a 3D effect from a 2D map.

The engine uses Pygame for rendering. The map of the game is represented as a 2D list, where each element represents a wall or an empty space. The engine also supports textured walls. The textures are loaded from image files and are mapped to the walls based on the distance and angle of the rays.

## 🎨 How to Change Images

To change the textures used in the game, you need to modify the `object_renderer` module. The textures are loaded in the `load_wall_textures` method of the `ObjectRenderer` class. Each texture is associated with a number, and these numbers are used in the game map to specify which texture to use for each wall.

To add a new texture, add a new line in the `load_wall_textures` method that associates a new number with the path to your image file. For example:

```python
3: self.get_texture(os.path.join(base_path, 'images', 'wall.jpg')),
```

## 🙏 Acknowledgements

I would like to express my appreciation to [TheAypisamFpv](https://github.com/TheAypisamFpv) for their  assistance in developing the maze generator for this project. Their expertise and support have been very usefull in bringing this project to life.

I'd also like to take this opportunity to thank the Coder Space tutorial, which was a great help in my project.

This project would not have been possible without the support and contributions of the open-source community. Thank you to everyone who has contributed to the libraries and tools used in this project.