
# Docker Python webapp with Flask to check if an IP is part of AWS infrastructure

<p align="center">
    <a href="https://github.com/andreip024/checkawsip/commits/main" target="_blank">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/andreip024/checkawsip?color=blue">
	<a href="https://github.com/andreip024/checkawsip/commits/main" target="_blank">
    <img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/m/andreip024/checkawsip/main?color=blue">
    <a href="https://github.com/andreip024/checkawsip/issues" target="_blank">
    <img alt="GitHub issues" src="https://img.shields.io/github/issues-raw/andreip024/checkawsip?color=blue">
    <a href="https://github.com/andreip024/checkawsip/releases" target="_blank">
	<img alt="GitHub version" src="https://img.shields.io/github/v/release/andreip024/checkawsip?color=blue">
    <a href="https://github.com/andreip024/checkawsip/blob/main/LICENSE" target="_blank">
	<img alt="GitHub License" src="https://img.shields.io/github/license/andreip024/checkawsip?color=blue">
</p>

---

<p align="center">
  <a href="#about">About</a> •
  <a href="#variables">Variables</a> •
  <a href="#run-locally">Run locally</a> •
  <a href="#roadmap">Roadmap</a> •
  <a href="#changelog">Changelog</a> •
  <a href="#license">License</a> •
  <a href="#support">Support</a>
</p>
  <p align="center">
  This repository generates https://checkawsip.com

  ![Screenshot of the app](https://images-0168749535.s3.eu-central-1.amazonaws.com/checkawsip.com.jpg)
</p>

---

## About

Part of a cross-project with [TerraformAWSInfrastructure](https://github.com/andreip024/terraform-aws-infrastructure)

This project creates a simple and straightforward WebApp using Python with Flask where users can enter an IP address they want to check. When the user submits the IP address, the web app would use the public  AWS IP address range [JSON](https://ip-ranges.amazonaws.com/ip-ranges.json) to check if the IP address belongs to any of the AWS infrastructure.

The app is built and deployed using a Docker container to ensure consistency and ease of deployment across different platforms.

The Docker base image is ***python:3.9-slim-buster***

## Variables

| Variables name               |  Description                         |
|----------------|-------------------------------|
|SITE_KEY     |Site key (public) for Google reChapcha v3|
|SECRET_KEY   |Secret key (private) for Google reChapcha v3|
|VERIFY_URL   |Google URL for reChapcha - **DO NOT EDIT**|
|ANALYTICS_ID |Code for Google Analytics|
|AWS_URL      |AWS IP Ranges URL - **DO NOT EDIT**|

## Run locally

To run this project localy you need to have [Docker](https://www.docker.com/products/docker-desktop/) installed.
Clone the project and in the folder of the project build the image using this command:

```docker build -t checkawsip```

After the image is build you start a container using:

```docker run -d -p 5000:5000 checkawsip```

And the app will be accessible on http://localhost:5000/

## Roadmap

- [X] Display the region of the IP Adress;
- [X] Add Google reCaptcha v3 integration;
- [X] Add Goolge Analytics integration;
- [X] Add logging;
- [X] Add last update from AWS on footer;
- [ ] Add contact page;
- [ ] Send logs in AWS CloudWatch;
- [ ] Add aditional information about the page in the footer;
- [ ] Build the image and push it to Docker Hub with GitHub Actions;
- [ ] Create a user registration and login flow (Cross feature with [Terraform infra](https://github.com/andreip024/terraform-aws-infrastructure));
- [ ] Store the sesion in AWS ElastiCache (Cross feature with [Terraform infra](https://github.com/andreip024/terraform-aws-infrastructure));
- [ ] Create saves in AWS DynamoDB for stats (Cross feature with [Terraform infra](https://github.com/andreip024/terraform-aws-infrastructure));
- [ ] Create a queue for requests with AWS SQS (Cross feature with [Terraform infra](https://github.com/andreip024/terraform-aws-infrastructure));
- [ ] Create an API for the app;

## Changelog

v1.1.0 [19-Apr-2023]

- Display the region of the IP Adress;
- Add Google reCaptcha v3 integration;
- Add Goolge Analytics integration;
- Add logging;
- Add last update from AWS on footer;

v1.0.0 [05-Apr-2023] 

- App release

## License

Distributed under the MIT License. See [LICENSE](https://github.com/andreip024/checkawsip/blob/main/LICENSE) for more information.

## Support

This repository is maintained actively, so if you face any issue or you want to propose new features, pelase [open an issue](https://github.com/andreip024/checkawsip/issues/new).


You can contact/find me also on:  
<a href="https://www.linkedin.com/in/andrei-p%C3%A2rv-53a91315a/">
<img alt="Linkedin" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white">
<a href="mailto:andreiparv@gmail.com">
<img alt="Gmail" src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white">


---

Liked the work? Give the repository a star!