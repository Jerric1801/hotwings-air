package com.hotwings.updatedelay.models;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@AllArgsConstructor
@NoArgsConstructor
@Builder
@Data
public class User {
    private String name;
    private String email;
    private String password;
    private int loyalty_points;
    private Object past_bookings;
    private Object upcoming_bookings;
}
