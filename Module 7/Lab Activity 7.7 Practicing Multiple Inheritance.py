# Write the TabletCamera class here 
class TabletCamera:
    def __init__(self, pixels):
        self.pixels = pixels

# Write the Facial_recognition class here
class Facial_recognition:
    def __init__(self):
        pass

    def scan_face(self):
        print("Scanning Face...")


# Write the BioTablet class here
class BioTablet(TabletCamera, Facial_recognition):
    def __init__(self, pixels):
        self.pixels = pixels
        pass

if __name__ == '__main__':

# Write an instance of the BioTablet class
    tablet = BioTablet("12MP")
# Call the scan_face method from the instance
    tablet.scan_face()
# Print the pixels from the instance
    print(tablet.pixels)
