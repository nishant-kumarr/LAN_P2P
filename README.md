# Peer-to-Peer File Transfer System

## Overview

This project implements a simple Peer-to-Peer (P2P) file transfer system using Python. The sender and receiver communicate over a local area network to transfer a file. P2P systems allow direct communication between peers without the need for a central server, providing advantages as discussed below.

## Advantages of Peer-to-Peer

1. **Decentralization:** P2P systems eliminate the need for a central server, distributing the workload across multiple peers.

2. **Scalability:** P2P networks can easily scale as more peers join, making them suitable for large-scale file sharing.

3. **Redundancy:** The distributed nature of P2P systems enhances data redundancy and fault tolerance.

4. **Efficiency:** Peers can directly communicate with each other, leading to faster file transfers and reduced network bottlenecks.

## Functionalities

### Sender (`Sender.py`)

1. **Socket Initialization:** Creates a socket for communication.
2. **File Selection:** Uses Tkinter to prompt the user to select a file for transfer.
3. **Connection Establishment:** Listens for incoming connections and establishes a connection with the receiver.
4. **File Size Transmission:** Sends the size of the selected file to the receiver.
5. **File Transmission:** Sends the file data in chunks to the receiver.

### Receiver (`Receiver.py`)

1. **Socket Initialization:** Creates a socket to connect to the sender.
2. **Connection Establishment:** Connects to the sender using the provided IP address and port.
3. **File Size Reception:** Receives the size of the incoming file.
4. **File Saving Dialog:** Prompts the user to select a location and name for the received file.
5. **File Reception:** Receives file data in chunks and saves it to the specified file.

## Libraries Used in this P2P File Transfer System

1. **Socket (`socket`):** For creating and managing network sockets to facilitate communication between the sender and receiver.
2. **Os (`os`):** For interacting with the operating system and retrieving information about the selected file, such as its size.
3. **Tkinter (`tkinter`):** A GUI toolkit used for building the user interface for the sender. It provides a file dialog for selecting the file to be sent and prompting the user for interaction.
4. **Filedialog (`tkinter.filedialog`):** A submodule of Tkinter specifically used to create file selection and saving dialogs. It simplifies the process of interacting with the file system, allowing users to choose a file for sending or specify the location to save the received file.
5. **Struct (`struct`):** Although not explicitly imported, it is implicitly used for converting file size to bytes and vice versa. This is done through the `to_bytes` and `from_bytes` methods for encoding and decoding integers.


## How to Use It

1. Run `Sender.py` on the machine you want to send the file from.
2. Note the IP address displayed by the sender.
3. Run `Receiver.py` on the machine you want to receive the file on.
4. Enter the sender's IP address when prompted.
5. Select a file for transfer on the sender side.
6. The file will be transferred and saved on the receiver side.

## Further Possible Expansions

1. **Security:** Implement encryption and authentication for secure file transfers.
2. **User Interface:** Develop a more user-friendly graphical user interface (GUI) using a dedicated framework.
3. **Error Handling:** Enhance error handling to provide better feedback to users in case of connection issues or file transfer failures.
4. **Concurrency:** Use threading to handle multiple file transfers simultaneously.
5. **Protocol Enhancements:** Design a custom protocol to support additional functionalities, such as resuming interrupted transfers or providing file metadata.

## Note

To gain a deeper understanding and clearer insights into the Peer-to-Peer File Transfer System, it is recommended to refer to the accompanying report and PowerPoint presentation. These supplementary materials provide a comprehensive overview, detailed explanations, and visual aids to enhance your comprehension of the project.

## Contributors

This Peer-to-Peer File Transfer System is brought to you by:

- [Viswanadha sai nissankararao](https://github.com/createunique)
- [Nishant Kumar (me)](https://github.com/nishant-kumarr)


<div> 
<h2 align = 'right'> Thank You !! </h2>
</div>
