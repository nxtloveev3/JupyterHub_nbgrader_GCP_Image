#Scripts for nbgrader configuration
#You needs to create this configuration file with content shown below in home directory (~/.jupyter/nbgrader_config.py), using a Linux text editor.

#Scripts Begin
##############################################################################################################################################################
# Initialize Configuration Object

c = get_config()

# Set Course Id for Better Organization

c.CourseDirectory.course_id = "your_course_name"

# Setup the Exchange Directory  for Releasing and Submitting Assignments

c.Exchange.root = "/tmp/exchange"
