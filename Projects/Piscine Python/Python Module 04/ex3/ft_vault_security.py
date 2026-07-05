#!/usr/bin/env python3
"""
Exercise 3: Vault Security
Implement secure file operations using the 'with' context manager
to ensure proper resource management and automatic vault sealing.
"""


def secure_extraction(filename: str) -> None:
    """
    Securely extract classified data from a vault using context manager.

    Args:
        filename: Path to the classified data vault.
    """
    print("SECURE EXTRACTION:")
    with open(filename, 'r') as vault:
        content = vault.read()
    for line in content.strip().split('\n'):
        print(line)


def secure_preservation(filename: str, data: str) -> None:
    """
    Securely preserve new information into a vault using context manager.

    Args:
        filename: Path to the target preservation vault.
        data: Data to inscribe into the vault.
    """
    print("SECURE PRESERVATION:")
    with open(filename, 'w') as vault:
        vault.write(data + '\n')
    print(data)
    print("Vault automatically sealed upon completion")


def vault_security_protocol() -> None:
    """
    Execute secure vault operations with failsafe protocols.
    Demonstrates automatic vault sealing via the 'with' statement.
    """
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")

    secure_extraction("classified_data.txt")

    secure_preservation(
        "security_protocols.txt",
        "[CLASSIFIED] New security protocols archived"
    )

    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    vault_security_protocol()
