# BHEEM (An Advance Recon Tool)
A tool which can perform advance recon automatically. Sit back and enjoy this tool work for you and find target's subdomains automatically. This tool also find you a bug bounty targets for you not only Hackerone, Intigrity, Bugcrowd but this find VRPs which is not included in platforms. This tool has various features like Finding you a Target, Automatic find subdomains, Detect CMS, Honeypot, WAF, Also find SQLi, XSS through subdomains etc.

# HOW TO RUN THIS TOOL

Run this tool as a root

you need some following tools to run this tool

1. subfinder
2. httpx
3. amass
4. waybackurls
5. gf and gf-patterns

1.) install subfinder : 
	
	GO111MODULE=on go get -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder

2.) install httpx:

	GO111MODULE=on go get -v github.com/projectdiscovery/httpx/cmd/httpx

3.) install amass:
	
	apt-get install amass

4.) install waybackurls

	go get github.com/tomnomnom/waybackurls

5.) gf and gf-patterns

	a.) go get -u github.com/tomnomnom/gf
	
	b.) if your cmd is bash:
		
		echo 'source $GOPATH/src/github.com/tomnomnom/gf/gf-completion.bash' >> ~/.bashrc
		source ~/.bashrc
	
	if your cmd is zsh:

		echo 'source $GOPATH/src/github.com/tomnomnom/gf/gf-completion.bash' >> ~/.zshrc
		source ~/.zshrc

	c.) mkdir .gf
	d.) cp -r $GOPATH/src/github.com/tomnomnom/gf/examples ~/.gf
	e.) git clone https://github.com/1ndianl33t/Gf-Patterns
	f.) mv ~/Gf-Patterns/*.json ~/.gf 	
  
# INSTALLATION

1.) Download all files...!!

2.) install requirements.txt:

    pip3 install -r requirements.txt

3.) Run bheem.py file:

    python3 bheem.py

# CREDITS

[!] Created by : Devarsh Parmar (STARLORD_3307)

[-] Linkedin : https://www.linkedin.com/in/devarsh-parmar-992b5b169

[!] Idea behind of this tool suggested by : Zeel Patel (Cyber Zeel)

[-] Website : www.spinthehack.in
	
[-] https://linktr.ee/spinthehack
