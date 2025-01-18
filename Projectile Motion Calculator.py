import math



def get_input():
    
  """Gets input from the user and validates it."""
  


  while True:
      
    try:
        
      initial_velocity = float(input("Enter the initial velocity (m/s): "))
      
      launch_angle = float(input("Enter the launch angle (degrees): "))
      
      initial_height = float(input("Enter the initial height (m): "))
      


      if initial_velocity >= 0 and 0 <= launch_angle <= 90 and initial_height >= 0:
          
        break
    
      else:
          
        print("Invalid input. Please ensure velocity, angle, and height are non-negative.")
        
    except ValueError:
        
      print("Invalid input. Please enter numbers only.")
      


  return initial_velocity, math.radians(launch_angle), initial_height



def calculate_max_height(initial_velocity, launch_angle, initial_height):
    
  """Calculates the maximum height of the projectile."""
  


  v_y = initial_velocity * math.sin(launch_angle)
  
  g = 9.81  # Acceleration due to gravity (m/s^2)
  
  max_height = initial_height + (v_y**2) / (2 * g)
  
  return max_height



def calculate_range(initial_velocity, launch_angle, initial_height):
    
  """Calculates the horizontal range of the projectile."""
  


  g = 9.81  # Acceleration due to gravity (m/s^2)
  
  time_of_flight = (initial_velocity * math.sin(launch_angle) +
                    
                    math.sqrt((initial_velocity * math.sin(launch_angle))**2 + 2 * g * initial_height)) / g
  
  range_x = initial_velocity * math.cos(launch_angle) * time_of_flight
  
  return range_x



if __name__ == "__main__":
    
  initial_velocity, launch_angle, initial_height = get_input()
  


  while True:
      
    choice = input("What do you want to calculate? (Max Height/Range/Exit): ").lower()
    


    if choice == "max height":
        
      max_h = calculate_max_height(initial_velocity, launch_angle, initial_height)
      
      print(f"The maximum height reached is: {max_h:.2f} meters")
      
    elif choice == "range":
        
      range_x = calculate_range(initial_velocity, launch_angle, initial_height)
      
      print(f"The horizontal range is: {range_x:.2f} meters")
      
    elif choice == "exit":
        
      break
    
    else:
        
      print("Invalid choice. Please try again.")
