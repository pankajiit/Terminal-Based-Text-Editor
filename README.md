## Terminal-Based Text Editor with DSA

## Reasons for Choosing This Project:
Editors like Notepad and VSCode are everyday tools for tasks like coding and note-taking. Understanding their inner workings reveals the challenges developers face and the strategies they employ. This project offers an excellent opportunity to apply various DSA concepts, such as linked lists, tries, and string matching algorithms, in a real-world scenario.



## Research and Creation of Detailed Outline Document:

  # Introduction
  
      The Terminal-Based Text Editor with DSA is a project aimed at developing a text editor application in the terminal environment. The objective is to implement essential functionalities such as text manipulation, search, replace, and file operations using Data Structures and Algorithms (DSA) concepts.
  
  # Functionalities:
      
      Text Manipulation: Users can insert, delete, and edit text at any position within the document.
      
      Search Functionality: Implement a search feature allowing users to find specific words or phrases within the content.
      
      Replace Functionality: Allow users to replace occurrences of a specified word with another throughout the document.
      
      File Operations: Provide functionalities to load and save text files.
  
  
  # Technology Stack
  
      Programming Language: Python
      
      Libraries: Curses
      
      DSA Components: Linked Lists, Tries
      
      Data Structures and Algorithms
           WordNode: Represents individual words within the text.
          LineNode: Represents lines of text, consisting of a linked list of WordNodes.
         Trie: Utilized for efficient search and replacement operations, indexing words along with their positions.
         
  # Implementation Details
  
     Text Manipulation:
     
          Implemented using LinkedLists where each LineNode contains a linked list of WordNodes.
          Insertion, deletion, and editing operations are performed by manipulating WordNodes within LineNodes.
          
    Search Functionality:
    
            Trie data structure is used to index words or word addresss of all occurance for efficient search operations.
           
            
   Replace Functionality:
   
            Traverse through each word in the text, replacing occurrences of the old word with the new word.
            Update the Trie data structure to reflect changes after replacement.
            
    File Operations:
    
        save the data as a file and open the file for read, update the content .
  




## High-Level Design:

    User Interface Layer: Terminal-based interface for accepting user inputs and displaying text content.
    
    Text Editor Core: Implements text manipulation, search, replace, and file operations using LinkedLists and Trie data structures.
    
    Data Structures Layer: Consists of LineNode and WordNode structures for representing text content efficiently.
    
    Algorithm Layer: Utilizes Trie for optimized search and replace operations.
    
    File Operations Layer: Handles loading and saving text files
