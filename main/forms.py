from django.forms import ModelForm
from main.models import ItemEntry

class ItemEntryForm(ModelForm):
    class Meta:
        model = ItemEntry
        fields = ["name", "price", "description", "quantity", "image"]
        def clean_name(self):
            name = self.cleaned_data["name"]
            return strip_tags(name)

        def clean_price(self):
            price = self.cleaned_data["price"]
            return strip_tags(price)
        
        def clean_description(self):
            description = self.cleaned_data["description"]
            return strip_tags(description)
        
        def clean_quantity(self):
            quantity = self.cleaned_data["quantity"]
            return strip_tags(quantity)
        
        def clean_image(self):
            image = self.cleaned_data["image"]
            return strip_tags(image)