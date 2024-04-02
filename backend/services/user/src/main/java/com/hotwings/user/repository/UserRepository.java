package com.hotwings.user.repository;

import com.hotwings.user.models.User;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;

import java.util.List;
import java.util.Optional;

public interface UserRepository extends MongoRepository<User, String> {
    Optional<User> findOneByEmailAndPassword(String email, String password);

    Optional<User> findOneByUseridAndEmail(String userid, String email);

    Optional<User> findOneByEmail(String email);

    @Query(" { 'upcoming_bookings.date': ?0, 'upcoming_bookings.flight_id': ?1 } ")
    List<User> findByDisruptedFlight(String date, String flightId);
}
