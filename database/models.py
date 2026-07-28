from datetime import datetime
from sqlalchemy import BigInteger, String, Boolean, Float, DateTime, ForeignKey, Text, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    username: Mapped[str | None] = mapped_column(String(64), nullable=True)
    first_name: Mapped[str] = mapped_column(String(64))
    language: Mapped[str] = mapped_column(String(5), default="en")
    is_premium: Mapped[bool] = mapped_column(Boolean, default=False)
    is_banned: Mapped[bool] = mapped_column(Boolean, default=False)
    referrer_id: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    alerts: Mapped[list["Alert"]] = relationship("Alert", back_populates="user", cascade="all, delete")
    watchlist: Mapped[list["Watchlist"]] = relationship("Watchlist", back_populates="user", cascade="all, delete")

class Alert(Base):
    __tablename__ = "alerts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id"))
    symbol: Mapped[str] = mapped_column(String(20))
    target_price: Mapped[float] = mapped_column(Float)
    is_triggered: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    user: Mapped["User"] = relationship("User", back_populates="alerts")

class Watchlist(Base):
    __tablename__ = "watchlist"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id"))
    symbol: Mapped[str] = mapped_column(String(20))
    asset_type: Mapped[str] = mapped_column(String(10), default="crypto") # 'crypto' or 'forex'

    user: Mapped["User"] = relationship("User", back_populates="watchlist")
