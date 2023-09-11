#  Sample API

## Description

This is a sample FastAPI project that demonstrates how to set up a simple FastAPI web server that serves an HTML page.

## Prerequisites

- [Conda](https://docs.anaconda.com/anaconda/install/)

## Getting Started

```bash
git clone https://github.com/cyberkatze/sample_api.git
```

## Create and Activate Conda Environment

Create a new Conda environment based on the `environment.yml` file.

```bash
conda env create -f environment.yml
```

Activate the newly created Conda environment.

```bash
conda activate sample_api
```

### Step 4: Run the FastAPI Server

Run the FastAPI server using Uvicorn.

```bash
uvicorn app:app --reload
```

### Step 5: Access the API

Open your web browser and navigate to `http://127.0.0.1:8000/` to see the HTML page served by FastAPI.

---

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

