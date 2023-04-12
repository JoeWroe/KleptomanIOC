<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
[![Build][build-shield]][build-url]
[![Contributors][contributors-shield]][contributors-url]
[![Open Issues][open-issues-shield]][projects-url]
[![Closed Issues][closed-issues-shield]][projects-url]
[![License][license-shield]][license-url]

# KleptomanIOC

## About The Project

A tool for swiping Indicators Of Compromise (IOC's) from data.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

### Prerequisites

- Python 3.10
    - [Pyenv](https://github.com/pyenv/pyenv) is a good option for managing your Python versions.
- Pipenv
    - [Pipenv](https://pipenv.pypa.io/en/latest/) recommends installing via pip.
    - [Homebrew](https://formulae.brew.sh/formula/pipenv) also provides a formula.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/JoeWroe/KleptomanIOC
   ```

2. Build a virtual environment
   ```sh
   pipenv --python 3.10
   ```

3. Install dependencies
   ```sh
   pipenv install --dev
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Usage

From the root of the cloned repository:

```sh
python run kleptomanioc
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contributing

If you wish to contribute to this project, please feel free to raise draft stories on our project board, open issues, and submit pull requests. Conversation, opinions and ideas are just as valuable as code; please don't be shy.

### Roadmap

[Github Projects Board](https://github.com/users/JoeWroe/projects/1/views/1)

### Submitting pull requests

Our pipeline will run against any code commit or pull request to our main branch. We run tests and checks in the pipeline, but it is always a good idea to perform them locally first.

#### Running unit tests

```sh
pipenv run unit-test
```

#### Running code style checks

```sh
pipenv run style-check
```

#### Obtaining a test code coverage report

```sh
pipenv run code-coverage
```

You will then see a simple coverage output in your terminal. Look in the newly created folder `cov_html/` for more information. You can use a browser to open the `index.html` file.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## License

Distributed under the GPL-3.0 License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Acknowledgments

* [Choose an Open Source License](https://choosealicense.com)
* [Best-README-template](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[build-shield]: https://img.shields.io/github/actions/workflow/status/JoeWroe/KleptomanIOC/build_and_test.yml?style=for-the-badge
[build-url]: https://github.com/JoeWroe/KleptomanIOC/actions/workflows/build_and_test.yml
[contributors-shield]: https://img.shields.io/github/contributors/JoeWroe/KleptomanIOC?color=informational&style=for-the-badge
[contributors-url]: https://github.com/JoeWroe/KleptomanIOC/graphs/contributors
[open-issues-shield]: https://img.shields.io/github/issues/JoeWroe/KleptomanIOC?style=for-the-badge
[closed-issues-shield]: https://img.shields.io/github/issues-closed/JoeWroe/KleptomanIOC?style=for-the-badge
[projects-url]: https://github.com/users/JoeWroe/projects/1/views/1
[license-shield]: https://img.shields.io/github/license/JoeWroe/KleptomanIOC?style=for-the-badge
[license-url]: https://github.com/JoeWroe/KleptomanIOC/blob/main/LICENSE
