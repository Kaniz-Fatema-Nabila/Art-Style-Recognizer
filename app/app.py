from fastai.vision.all import load_learner
import gradio as gr

art_labels= [
    "Art Nouveau",
    "Constructivism Art",
    "Cubism Art",
    "Dadaism Art",
    "Fauvism Art",
    "Gothic Art",
    "Minimalism Art",
    "Pointillism Art",
    "Pop Art",
    "Prehistoric Art"
    ]

model = load_learner('models/artStyle_recognizer-v5.pk1')

def recognize_image(image):
    _, _, probs = model.predict(image)
    return dict(zip(art_labels, map(float, probs)))

image = gr.inputs.Image()
label = gr.outputs.Label()
example = [
    'Art Nouvaeu.jpg',
    'Constructivism art.jpg',
    'Fauvism art.jpg',
    'Gothic art.jpeg',
    'Minimalistic art.jpg' 
]

iface = gr.Interface(fn = recognize_image, inputs= image, outputs = label, examples = example)
iface.launch(inline=False, share=True)
