from scraper import scrape
if __name__ == '__main__':
    with open('emails.txt', 'r') as file:
        emails = [line.strip().split('@')[1] for line in file]
    providers = scrape(emails)
    with open('results.txt', 'w') as file:
        for e in range(len(emails)):
            file.writelines(f'{emails[e]}: {providers[e]}\n')