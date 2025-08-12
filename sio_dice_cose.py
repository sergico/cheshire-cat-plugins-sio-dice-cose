from cat.mad_hatter.decorators import tool
import random 

@tool(
   return_direct=True,
   examples=["tell a joke", "barzelletta"]
)
def sio_dice_cose(tool_input, cat):
   """
   Sio tells a random joke
   input is not ignored
   """

   jokes_image_list = [
      "1dd8c2106e309f74914e12a21456a69b.jpg",
      "5ca3622df40c2b44fadd9d6fced107e1.jpg",
      "cb4f4ef498b34b2a1eb2d562d94416ee.jpg"
   ]

   joke_image = random.choice(jokes_image_list)
   joke_image_path = f"/static/{joke_image}"

   return f"<img src='{joke_image_path}'/>"




