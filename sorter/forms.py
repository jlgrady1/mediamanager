import validate
from django import forms

class SetupForm(forms.Form):
    scan_folder = forms.CharField(required=True)
    destination_folder = forms.CharField(required=True)

    def clean_scan_folder(self):
        sf = self.cleaned_data['scan_folder']
        sf  = sf.rstrip('/') # Remove trailing slash (Linux)
        validate.folder_exists(sf) # Validate scan folder exists
        return sf

    def clean_destination_folder(self):
        sf = self.cleaned_data['scan_folder']
        df = self.cleaned_data['destination_folder']
        df  = df.rstrip('/') # Remove tailing slash (Linux)
        validate.folder_exists(df) # Validate destination exists
        validate.folder_writable(df) # Validate destination is writable
        if df == sf: # Validate source and destination are not the same
            raise ValidationError('Scan and Destination folders cannot be the same')
        return df