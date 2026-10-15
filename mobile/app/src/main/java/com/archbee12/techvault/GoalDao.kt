// Identifies the package containing this file.
package com.archbee12.techvault

// Imports the annotation that identifies a DAO interface.
import androidx.room.Dao
// Imports the annotation for deleting, inserting, querying and updating a database record.
import androidx.room.Delete
import androidx.room.Insert
import androidx.room.Query
import androidx.room.Update
import kotlinx.coroutines.flow.Flow

// Defines how learning goals are saved and retrieved.
@Dao
interface GoalDao {
    // Retrieves every goal, with the newest inserted IDs first.
    @Query("SELECT * FROM learning_goals ORDER BY id DESC")
    fun getAllGoals(): Flow<List<LearningGoal>>

    // Saves a new goal in the database.
    @Insert
    suspend fun insertGoal(goal: LearningGoal)

    // Updates an existing goal, such as changing its completion status.
    @Update
    suspend fun updateGoal(goal: LearningGoal)

    // Removes the specified goal from the database.
    @Delete
    suspend fun deleteGoal(goal: LearningGoal)
}