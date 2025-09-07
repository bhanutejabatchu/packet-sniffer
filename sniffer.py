from scapy.all import sniff

# File to save captured packets
log_file = "captures/packets.txt"

# Function to handle packets
def packet_callback(packet):
    # Print packet on console
    print(packet.summary())

    # Save packet details to file
    with open(log_file, "a") as f:
        f.write(packet.summary() + "\n")

print("[*] Starting packet sniffer...")
print("[*] Capturing 10 packets...")

# Capture 10 packets
sniff(prn=packet_callback, count=10)

print(f"[*] Packets saved to {log_file}")
