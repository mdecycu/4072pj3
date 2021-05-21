import pythoncom
import win32com.client
import win32api
import os


class inv:
    def __init__(self):
        """     Initialize the settings of the Inventor     """
        self.invApp = win32com.client.Dispatch("Inventor.Application")
        self.invApp.Visible = True
        self.invApp.SilentOperation = True

    def open(self, partName: str):
        """     Open Part     """
        try:
            self.oDoc = self.invApp.Documents.Open(partName)
        except:
            print("The part opened error !!")
        
    def parameter(self, **kwargs):
        """     Modify the dimension of the part     """
        for key, value in kwargs.items():
            # print(key, value)
            try:
                par = self.oDoc.ComponentDefinition.Parameters.Item(str(key))
            # Convert the unit from "cm" to "mm"
                par.Value = value * (10**-1)
            except:
                print(f"\"{key}\" is not the parameter in part")
                break
            
        is_update = self.oDoc.Update()
        if is_update == None:
            print("The part is updated.")
        else:
            print("Fail !")

    def save_as(self, newfilename: str):
        """     Save as the new part     """
        # Use the absolute path is better.
        self.oDoc.SaveAs(newfilename, True)
        print("Save succuessfully !")
        
    def close(self):
        """     Close Inventor     """
        self.invApp.Quit()


def link_gen_import_test():
    filename = os.path.basename(__file__)
    return filename + " import successfully !"


if __name__ == "__main__":
    inv = inv()


    inv.open('E:/4072pj3/project3/bike/binary_link.ipt')
    inv.parameter(
        # binary link
        center_distance=47,
        hole=10,
        thickness=5
    )

    
    """
    inv.open('E:/4072pj3/project3/40723145/ternary_link.ipt')
    inv.parameter(
        # ternary link
        center_distance1=513,
        center_distance2=198,
        center_distance3=405,
        hole=10,
        thickness=5
    )
    

    

    inv.open('G:/4072pj3/project3/bike/Slider1.ipt')
    inv.parameter(
        # slide block
        center_distance1=10,
        center_distance2=10,
        hole=10,
        thickness1=5,
        thickness2=170,
        slide_diameter=19
    )

    inv.open('G:/4072pj3/project3/bike/Slider.ipt')
    inv.parameter(
        # slide
        center_distance1=15,
        hole1=20,
        hole2=10,
        thickness1=96.127,
        thickness2=70,
        thickness3=5,
        slide_diameter=36.544
    )

        """
    
    inv.save_as("E:/4072pj3/project3/40723102/Firebird 29 bike/Binary link47.ipt")
    