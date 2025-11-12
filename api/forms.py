from django import forms
from .models import Review, Profile # Importamos los modelos de reseñas y perfil

# Estilos base de CSS/Tailwind para los campos
BASE_INPUT_CLASSES = 'mt-1 block w-full border border-gray-300 rounded-md shadow-sm focus:ring-[#6F4E37] focus:border-[#6F4E37] sm:text-sm p-2'
BASE_FILE_CLASSES = 'mt-1 block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-[#D2B48C] file:text-[#4A2312] hover:file:bg-[#6F4E37] hover:file:text-white'


# ----------------------------------------------------------------------
# 🌟 FORMULARIO 1: Para crear una nueva Reseña
# ----------------------------------------------------------------------
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        # Pedimos calificación, comentario e imagen opcional
        fields = ['rating', 'comment', 'image']
        
        widgets = {
            'rating': forms.Select(attrs={'class': BASE_INPUT_CLASSES}),
            'comment': forms.Textarea(attrs={'class': BASE_INPUT_CLASSES, 'rows': '4'}),
            # Usamos ClearableFileInput para permitir al usuario borrar la imagen si quiere
            'image': forms.ClearableFileInput(attrs={'class': BASE_FILE_CLASSES}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].label = 'Foto (Opcional)'


# ----------------------------------------------------------------------
# 🌟 FORMULARIO 2: Para subir o cambiar el Avatar del Usuario
# ----------------------------------------------------------------------
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        # Solo pedimos el campo 'avatar'
        fields = ['avatar']
        
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class': BASE_FILE_CLASSES}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['avatar'].label = 'Cambiar Avatar (JPG/PNG)'