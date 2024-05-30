# FloraFriend

FloraFriend is a garden management application that allows users to create, manage, and monitor gardens and plants. The application enables users to create new gardens, add plants and decorations, and monitor watering schedules with notifications for plant care.

## Features

- **Create Garden**: Users can create new gardens by setting up the layout and appearance of the garden based on a grid of squares (board), where various elements such as plants and decorations can be placed.
- **Delete Garden**: Ability to delete existing gardens.
- **Load Garden**: Allow loading of existing gardens.
- **Decorations**: Ability to add decorations that can be freely placed and moved around the garden.
- **Plants**:
  - Each plant has properties such as type, species, watering frequency, and additional fields requiring information on care frequency (e.g., pruning every 3 months).
  - Ability to group plants to treat them as a unit, for example, in the case of larger plants.
- **Garden Management**:
  - Remove Plants: Users can remove plants from the garden.
  - Watering Plants: The application monitors the watering schedule of the plants and sends notifications when it's time to water them.
  - Marking Weather: Users can mark if it rained on a given day.
  - Additional plant list view: Available list of plants with information on the next required watering.
- **Notifications**: FloraFriend will send notifications to the user about the need to water the plants when the appropriate time comes.

## Technologies

- **Python**: Programming language used to implement the application logic.
- **Tkinter**: Library for creating the user interface (GUI).
- **Plyer**: Library for sending system notifications.
- **win10toast**: Alternative library for sending system notifications on Windows.
- **JSON**: Format for managing garden data.
- **Datetime**: Module for managing time and plant watering schedules.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/JedrzejSobkow/FloraFriend.git
   cd FloraFriend
