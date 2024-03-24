package com.hotwings.user;

import com.hotwings.user.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.data.mongodb.repository.config.EnableMongoRepositories;

import java.util.Optional;

@SpringBootApplication
@EnableMongoRepositories
public class UserApplication {

	@Autowired
	UserRepository userRepo;

	public static void main(String[] args) {
		SpringApplication.run(UserApplication.class, args);
	}
}
