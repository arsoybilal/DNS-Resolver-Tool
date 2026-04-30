import dns.resolver
from colorama import Fore, Style, init

init(autoreset=True)

def resolve_dns(domain):
    record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'CNAME']
    
    print(f"\n{Fore.CYAN}--- {domain} için DNS Kayıtları Sorgulanıyor ---{Style.RESET_ALL}\n")

    for record in record_types:
        try:
            answers = dns.resolver.resolve(domain, record)
            print(f"{Fore.GREEN}[+] {record} Kayıtları:{Style.RESET_ALL}")
            for rdata in answers:
                print(f"  - {rdata}")
        except dns.resolver.NoAnswer:
            print(f"{Fore.YELLOW}[!] {record} kaydı bulunamadı.{Style.RESET_ALL}")
        except dns.resolver.NXDOMAIN:
            print(f"{Fore.RED}[-] Alan adı mevcut değil (NXDOMAIN).{Style.RESET_ALL}")
            return
        except Exception as e:
            print(f"{Fore.RED}[-] {record} sorgulanırken hata oluştu: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    target_domain = input("Sorgulamak istediğiniz domaini girin (örn: google.com): ")
    resolve_dns(target_domain)