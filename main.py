def main():
    import torch
    print(torch.__version__)
    print(torch.backends.mps.is_available())
    print(torch.backends.mps.is_built())


if __name__ == "__main__":
    main()
