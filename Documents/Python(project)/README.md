# Vehicle Rental System (VRS)

A Python-based console application for managing vehicle rentals with support for cars and bikes.

## Features

- **View Vehicles**: Display all vehicles or only available vehicles
- **Rent a Vehicle**: Rent cars or bikes by specifying rental duration
- **Return a Vehicle**: Mark rented vehicles as available
- **Admin Functions**: Add or remove vehicles from the system
- **Real-time Pricing**: Calculate rental costs based on hourly rates
- **Rental Tracking**: Keep track of who has rented a vehicle and until when

## Project Structure

```
VRS.py          # Main application file
```

## Classes

### Vehicle
Base class for all rental vehicles.
- **Attributes**: vehicle_id, brand, model, price_per_hour, is_available, rented_by, rented_until
- **Methods**: show_details()

### Car
Subclass of Vehicle representing cars.

### Bike
Subclass of Vehicle representing bikes.

### RentalSystem
Manages all rental operations.
- **Methods**:
  - `list_vehicles()` - Display all or available vehicles
  - `find_vehicle()` - Search for a vehicle by ID
  - `rent_vehicle()` - Rent a vehicle to a customer
  - `return_vehicle()` - Mark a vehicle as returned
  - `add_vehicle()` - Add a new vehicle (admin)
  - `remove_vehicle()` - Remove a vehicle (admin)

## Sample Vehicles

The system comes pre-loaded with:
- **C001**: Hyundai i10 (₹50/hr)
- **C002**: Maruti Swift (₹70/hr)
- **B001**: Honda CB Shine (₹20/hr)
- **B002**: TVS Apache (₹30/hr)

## Menu Options

1. **Show all vehicles** - View complete vehicle inventory
2. **Show available vehicles** - View only available vehicles for rental
3. **Rent a vehicle** - Rent a car or bike
4. **Return a vehicle** - Return a rented vehicle
5. **Add vehicle (admin)** - Add a new vehicle to inventory
6. **Remove vehicle (admin)** - Remove a vehicle from inventory
7. **Exit** - Close the application

## How to Use

### Prerequisites
- Python 3.x

### Running the Application

```bash
python VRS.py
```

### Example Workflow

1. Run the application
2. Choose option "2" to view available vehicles
3. Choose option "3" to rent a vehicle (e.g., C001)
4. Enter your name and rental duration in hours
5. The system calculates and displays the total cost
6. Choose option "4" to return the vehicle

## Dependencies

- `datetime` (standard library) - For managing rental dates and times

## License

This project is open source and available for educational purposes.

## Author

Created as a Vehicle Rental Management System project.
