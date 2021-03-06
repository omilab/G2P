# G2P


<!--
*** Thanks for checking out this README Template. If you have a suggestion that would
*** make this better please fork the repo and create a pull request or simple open
*** an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/omilab/G2P/">
    <img src="https://raw.githubusercontent.com/omilab/G2P/master/Img/Logo.png" alt="Logo" width="180" height="180">
  </a>
  
  <p align="center">
     <a href="https://drive.google.com/open?id=1Y5u8xfDDkP7rizKRLuVtHm2YuOIHpp_w">
    <img src="https://raw.githubusercontent.com/omilab/G2P/master/Img/ganan.PNG" alt="Ganan" width="240" height="120">
  </a>
  </p>
  <h3 align="center">G2P</h3>

  <p align="center">
    Grapheme to phoneme Dummy converter - Python GUI
    <br />
    <a href="https://drive.google.com/open?id=1Y5u8xfDDkP7rizKRLuVtHm2YuOIHpp_w"><strong>Download Current Version »</strong></a>
    <br />
    <br />
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)




<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

The Grapheme to phoneme dummy converter tool is a Graphical user interface (GUI) for a script develpoed in The Open Media and Information Lab (OMILab). The tool convert a given ortographic text to it's phonemic represintation based on a given lexicon.
This converter can be used for any Source to Target representations.

### Built With
* Python 3.6
* TKinter
* PIL



<!-- GETTING STARTED -->
## Getting Started

The G2P tool have no installation and work as a single file portable version, just download the latest version and run.

### Prerequisites

None



<!-- USAGE EXAMPLES -->
## Usage
### Lexicon
The Lexicon structure is as follows

| Source       | Target      |
| ------------- | ------------- |
| 0             | Efes          |
| את            | et            |

There is no need for headers but they can be added.

Note: In case of missing words in the lexicon the GUI let you choose between 2 options:
* Missing - Replace the missing word with "Missing"
* Source - Leave the missing word as it appears in the text file

The lexicon must be in CSV format

### Converting
First load the Lexicon in CSV format and the text file for conversion.
Once both are loaded a "Save" button will appear.
Save the converted file.





<!-- CONTRIBUTING -->
## Authers & Contributers

* Carmi Nehoray
* Dr. Silber-Varod Vered
* Amit Daphna



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Twitter - [@OmilabOpenu](https://twitter.com/OmilabOpenu)

Project Link: [https://github.com/omilab/G2P](https://github.com/omilab/G2P)









<!-- MARKDOWN LINKS & IMAGES -->
[build-shield]: https://img.shields.io/badge/build-passing-brightgreen.svg?style=flat-square
[contributors-shield]: https://img.shields.io/badge/contributors-1-orange.svg?style=flat-square
[license-shield]: https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square
[license-url]: https://choosealicense.com/licenses/mit
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: https://raw.githubusercontent.com/omilab/G2P/master/Img/g2p.PNG

