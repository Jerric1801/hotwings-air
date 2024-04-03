package com.hotwings.updatedelay.dto;

import com.hotwings.updatedelay.models.User;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.List;

@Data
@Builder
@AllArgsConstructor
@NoArgsConstructor
public class ItineraryMessage {
    private List<User> user_list;
    private String flight_id;
    private String departure;
    private String flight_number;
}
