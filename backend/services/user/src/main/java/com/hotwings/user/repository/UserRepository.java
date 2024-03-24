package com.hotwings.user.repository;

import com.hotwings.user.models.User;
import org.springframework.data.mongodb.repository.MongoRepository;

import java.util.Optional;

public interface UserRepository extends MongoRepository<User, String> {
    Optional<User> findOneByEmailAndPassword(String email, String password);

    Optional<User> findOneByEmail(String email);
}
