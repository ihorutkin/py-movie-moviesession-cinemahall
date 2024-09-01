from datetime import datetime

from django.db.models import QuerySet

from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int,
) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id,
    )


def get_movies_sessions(session_date: str | None = None) -> QuerySet:
    queryset = MovieSession.objects.all()
    if session_date:
        target_time = session_date
        queryset = queryset.filter(show_time__date=target_time)

    return queryset


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(pk=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime | None = None,
        movie_id: int | None = None,
        cinema_hall_id: int | None = None
) -> None:
    movie_session = MovieSession.objects.filter(id=session_id)

    updating_data = {}
    if show_time:
        updating_data["show_time"] = show_time
    if cinema_hall_id:
        updating_data["cinema_hall_id"] = cinema_hall_id
    if movie_id:
        updating_data["movie_id"] = movie_id

    if updating_data:
        if "show_time" in updating_data:
            movie_session.update(show_time=show_time)

        if "cinema_hall_id" in updating_data:
            if CinemaHall.objects.filter(id=cinema_hall_id).exists():
                movie_session.update(cinema_hall_id=cinema_hall_id)

        if "movie_id" in updating_data:
            if Movie.objects.filter(id=movie_id).exists():
                movie_session.update(movie_id=movie_id)


def delete_movie_session_by_id(session_id: int) -> None:
    get_movie_session_by_id(session_id).delete()
