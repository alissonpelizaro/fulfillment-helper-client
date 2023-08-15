# Assistant Fulfillment Helper Client Example
_Author: Alisson Pelizaro_

This repository contains an example client that demonstrates the usage of the `assistant-fulfillment-helper` library. The `assistant-fulfillment-helper` library simplifies the creation of webhooks for intent nodes in the TOTVS Assistant platform. With just a few lines of code, you can create custom business rules within your own server infrastructure.

## Prerequisites

- Python 3.7 or higher.

## Getting Started

1. Clone this repository to your local machine.

2. Install the required dependencies using the following command:
   ```
   pip install -r requirements.txt  
   ```
3. Run the example client using the command:
   ```
   python my_app.py
   ```
## Purpose

The purpose of this client example is to demonstrate how to integrate and utilize the `assistant-fulfillment-helper` library to create a custom webhook server for intent nodes in the TOTVS Assistant platform. By following the example code in `main.py`, you can understand how to:

- Set up a FulfillmentHelper instance.
- Define intent callbacks using the `@fh.intent()` decorator.
- Handle intent-specific logic and return responses using `FulfillmentHelperResponse`.
- Start a local server to handle webhook requests from the Assistant.

## Usage

1. Install the required packages by following the prerequisites above.

2. Import the `FulfillmentHelper` class from the `assistant_fulfillment_helper` module.

3. Instantiate the `FulfillmentHelper` class and define intent callbacks using the `@fh.intent()` decorator.

4. Implement your custom business logic within the callback functions.

5. Run the example client and access the local server's endpoint to test the webhook locally.

## Additional Information

For more information on the `assistant-fulfillment-helper` library and its usage, please refer to the [official documentation](https://pypi.org/project/assistant-fulfillment-helper/).

## License

This example client is provided under the [MIT License](LICENSE).
