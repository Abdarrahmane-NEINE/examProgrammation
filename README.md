# Threading Oil Management System

## Overview
This project simulates an oil management system using Python's multithreading. It demonstrates how pumps (producers) and machines (consumers) work concurrently:
- **Pumps** add oil to a shared tank.
- **Machines** process the oil from the tank and update stock lists.
- **Thread Safety** is maintained by using locks (`tank_lock` and `stock_lock`) to protect shared data.

## Features
- **Multithreading:** Utilizes Python's `threading` module.
- **Shared Data Management:** Uses global lists for the oil tank and stock storage.
- **Synchronization:** Implements locks to prevent race conditions when accessing shared resources.
- **Scalability:** Easy to extend with additional threads representing different parts of the system.

## Requirements
- Python 3.x

## Running the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/Abdarrahmane-NEINE/taskFillTank.git
